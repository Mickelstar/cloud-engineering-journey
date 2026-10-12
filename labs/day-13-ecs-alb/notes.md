# Day 13 — ECS Fargate + Application Load Balancer Notes

## 1. Core Concepts

### Application Load Balancer (ALB)

Receives HTTP/HTTPS requests and forwards them to registered targets.

### Target Group

Defines the destinations that receive traffic and performs health checks.

For Fargate tasks using `awsvpc` networking, the target type must be **IP addresses**.

### ECS Service

Maintains the desired number of running tasks and integrates with load balancing.

### AWS Fargate

Runs containers without requiring management of the underlying EC2 servers.

### Amazon ECR

Stores the container images that Fargate retrieves to start tasks.

## 2. Request Flow

```text
Browser
   |
   v
ALB DNS
   |
   v
ALB Listener :80
   |
   v
Target Group
   |
   v
Healthy Fargate Task :80
   |
   v
NGINX Application
```

## 3. Security Group Chain

```text
Internet
   |
   v
CloudEngineer-ECS-ALB-SG
Inbound TCP 80 from 0.0.0.0/0
   |
   v
CloudEngineer-ECS-Task-SG
Inbound TCP 80 from ALB security group
   |
   v
Fargate Container
```

The ALB accepts public HTTP traffic. The task security group accepts application traffic from the ALB security group rather than from arbitrary internet sources.

## 4. Target Group Health Checks

Configuration:

```text
Target group: CloudEngineer-ECS-TG
Protocol: HTTP
Port: 80
Path: /
Success codes: 200
```

Healthy targets are eligible to receive traffic.

If the ALB returns `503`, investigate:

1. Target registration
2. Target health and health-check reason
3. ECS task status
4. ECS service events
5. Security group rules and network connectivity

Do not assume that every `503` is an application-code problem.

## 5. Troubleshooting: ECR Connection Timeout

### Symptom

The ALB returned:

```text
503 Service Temporarily Unavailable
```

The target group initially had no registered targets.

### ECS event

Tasks could not pull the image from ECR. The event reported a connection timeout to the ECR API on TCP port 443.

### Checks performed

- ECS service networking configuration
- Public IP assignment
- Task security group outbound HTTPS
- Public subnet default route
- Internet Gateway attachment

### Resolution

The network configuration was checked and corrected as needed. The service was redeployed, the targets became healthy, and the application loaded through the ALB.

### Lesson

A container image pull requires network access to ECR. A running ECS cluster alone does not guarantee that tasks can retrieve their images.

For public-subnet Fargate tasks, public IP assignment and a valid route to an Internet Gateway can provide outbound connectivity, provided security rules permit it.

A private-subnet design generally requires NAT or the appropriate VPC endpoints for the necessary AWS services.

## 6. ECS vs. Fargate vs. ALB

| Component | Responsibility |
|---|---|
| ECR | Stores container images |
| ECS | Manages container workloads |
| Fargate | Supplies serverless container compute |
| ALB | Receives and distributes application traffic |
| Target group | Registers targets and checks their health |
| Security group | Controls allowed network traffic |

## 7. Cost Awareness

ALBs incur charges while provisioned. Fargate incurs compute charges while tasks run.

After validating the application:

- Set the ECS service desired count to zero.
- Stop the running tasks and delete the service.
- Delete the ALB.
- Delete the target group.
- Retain the ECR image and task definition for future use.

An empty ECS cluster can remain without running Fargate compute. Retained resources should still be reviewed periodically for potential charges.

## 8. Days 10–13: Complete Container Workflow

```text
Day 10: Docker builds and runs the image locally
                    |
                    v
Day 11: ECR stores the image
                    |
                    v
Day 12: ECS/Fargate runs the container
                    |
                    v
Day 13: ALB routes traffic to healthy Fargate tasks
```

## 9. Final Understanding

- **ECR:** Where the image is stored.
- **ECS:** How the container workload is managed.
- **Fargate:** Where the container runs without managing servers.
- **ALB:** How users reach the application through a load balancer.
- **Target group:** Which targets receive traffic and whether they are healthy.

## Day 13 — COMPLETE
