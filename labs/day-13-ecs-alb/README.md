# Day 13 — ECS Fargate with Application Load Balancer

## Objective

Deploy a containerized application using Amazon ECS, AWS Fargate, and an Application Load Balancer (ALB).

**What I accomplished:**

- Connected an ALB to an ECS Fargate service.
- Configured security groups to restrict direct access to containers.
- Registered Fargate tasks with a target group.
- Diagnosed and resolved an ECR connectivity issue.
- Verified application access through the ALB.
- Cleaned up billable resources after testing.

## Architecture

```text
                 Internet
                     |
                     v
            Application Load
               Balancer
             Port 80 (HTTP)
                     |
                     v
                Target Group
                     |
                     v
               ECS Service
                     |
              +------+------+
              |             |
              v             v
         Fargate Task 1  Fargate Task 2
              |             |
              +------+------+
                     |
                     v
               Docker Image
                from ECR
```

*The service was configured with a desired count of two tasks. ECS managed task placement and target registration.*

## AWS Resources

| Resource | Name |
|---|---|
| Region | `eu-north-1` |
| ECS cluster | `CloudEngineer-ECS-Cluster` |
| ECS service | `CloudEngineer-Web-Service` |
| Task definition | `CloudEngineer-Web-Task` |
| ALB | `CloudEngineer-ECS-ALB` |
| Target group | `CloudEngineer-ECS-TG` |
| ALB security group | `CloudEngineer-ECS-ALB-SG` |
| Task security group | `CloudEngineer-ECS-Task-SG` |
| ECR image | `cloud-engineer-web:v1` |

## Security Configuration

### ALB security group

- Allows inbound HTTP traffic on TCP port 80 from the internet.

### Fargate task security group

- Allows inbound TCP port 80 only from `CloudEngineer-ECS-ALB-SG`.
- Allows outbound HTTPS traffic needed to retrieve the image from ECR.

This establishes the intended traffic path:

```text
Internet → ALB → Fargate Tasks
```

Direct internet access to the container port is restricted by the task security group.

## Deployment and Validation

1. Created the ALB and target group.
2. Configured the ECS service to use the ALB.
3. Selected the existing Fargate task definition and ECR image.
4. Waited for the ECS tasks to start and register.
5. Verified the target group reported healthy targets.
6. Opened the ALB DNS address in a browser.
7. Confirmed the application loaded successfully.

**Result: Successful deployment and browser validation through the ALB.**

## Troubleshooting

Initially, the ALB returned `503 Service Temporarily Unavailable`, and the target group had no registered targets.

ECS service events revealed that tasks were unable to pull the container image from ECR because the connection timed out on TCP port 443.

The issue was resolved by checking the task networking configuration, public IP assignment, security group egress, and public subnet routes. After correcting the connectivity configuration and redeploying, the targets became healthy and the ALB served the application.

### Key lesson

A `503` from an ALB can indicate that no healthy targets are available. Check target health and ECS service events before changing the application or rebuilding the image.

## Cost Management

After successful validation:

- Reduced the ECS service desired count to zero and stopped the running tasks.
- Deleted the ECS service.
- Deleted the ALB.
- Deleted the target group.
- Retained the ECS cluster, task definition, ECR image, and security groups for future labs.

No NAT Gateway was created for this lab.

## Validation Checklist

- [x] ALB created and configured
- [x] Target group created
- [x] ECS service connected to ALB
- [x] Fargate tasks started successfully
- [x] Target health became healthy
- [x] Application loaded through ALB DNS
- [x] ECR connectivity issue resolved
- [x] Billable compute and ALB resources cleaned up
- [x] Lab documented

## Key Takeaways

- An ALB distributes incoming requests to registered targets.
- ECS manages the desired state of the container service.
- Fargate runs containers without requiring EC2 server management.
- Target groups perform health checks and route traffic to healthy targets.
- Security groups can restrict container traffic to the ALB.
- Public subnet routing, public IP assignment, and outbound connectivity matter when Fargate tasks need to pull images from ECR.

## Status

### Day 13 — COMPLETE
