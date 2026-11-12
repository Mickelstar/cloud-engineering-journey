# Day 12 — Amazon ECS on AWS Fargate

## Objective

Document the container deployment flow from a Docker image in Amazon Elastic Container Registry (ECR) to a task running on Amazon ECS with AWS Fargate.

## Deployment Flow

The original Day 12 README records this architecture:

```text
Docker Image
     |
Amazon ECR
     |
ECS Task Definition
     |
ECS Cluster
     |
AWS Fargate
     |
Running Container
     |
Public IP
     |
Browser
```

The accompanying notes also record the earlier container lifecycle:

```text
Dockerfile
    |
Docker Image
    |
Docker Container
```

## Core Components

| Component | Responsibility |
|---|---|
| Dockerfile | Defines how the application image is built. |
| Docker image | Packages the application and its runtime dependencies. |
| Amazon ECR | Stores and distributes the container image. |
| ECS task definition | Describes the container image and runtime configuration for a task. |
| ECS cluster | Logical grouping for ECS tasks and services. |
| AWS Fargate | Runs containers without requiring the user to manage EC2 container hosts. |

## Important Architecture Considerations

The original diagram ends at a public IP and browser. A public IP is one possible way to expose a task, but it is not a complete production ingress design.

For a production-minded deployment, evaluate:
- Running tasks in private subnets where appropriate.
- Using an Application Load Balancer for controlled HTTP/HTTPS ingress.
- Restricting task Security Group ingress to the load balancer.
- Defining CPU, memory, container ports, health checks, and logging in the task definition.
- Using an ECS service to maintain the desired number of tasks.
- Assigning least-privilege task execution and task roles.
- Storing secrets outside the image and source repository.

## Validation Evidence

The surviving Day 12 notes contain only a partial container lifecycle diagram, and the original README contains only the deployment flow. They do not preserve the cluster name, service or task-definition details, image URI, network configuration, deployment commands, or test results.

Accordingly, this document records the architecture and component responsibilities; it does not claim that a live ECS deployment or browser connectivity was independently verified from the available notes.

## Evidence to Add

To make this lab reproducible and portfolio-ready, add sanitized evidence for:
1. ECR repository and image tag/digest.
2. ECS cluster, service, and task-definition revision.
3. Task status and deployment events.
4. Subnet, public-IP, load-balancer, and Security Group configuration.
5. Application health-check result and the exact endpoint tested.
6. Cleanup performed and any AWS costs incurred.

**Day 12 status:** Deployment architecture documented; implementation and runtime validation evidence still need to be captured.
