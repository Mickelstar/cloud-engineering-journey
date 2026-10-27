# Day 21 — Secure Container Deployment on Amazon ECS Fargate

## Objective
Deploy the Day 20 URL phishing detector container to Amazon ECS Fargate using Amazon ECR and CloudWatch Logs.

## Implementation
- Built and pushed the container image to Amazon ECR (`cloud-engineer-web:day21`).
- Registered ECS Fargate task definition `day21-url-detector:1`.
- Configured 0.25 vCPU, 512 MiB memory, and a non-root container user (UID 10001).
- Configured CloudWatch logging at `/ecs/day21-url-detector`.
- Used the existing ECS task security group, allowing outbound TCP 443 and no inbound rules.
- Launched a temporary task in the subnet routed through the Internet Gateway, with a public IP enabled and no inbound security-group access.

## Validation
- Local container tests passed for `GET /health` and `POST /analyze`.
- ECS task reached `RUNNING`.
- CloudWatch Logs confirmed: `Detector API listening on port 8080`.
- The task was stopped after validation.

## Security and Cost Considerations
- Container runs as a non-root user.
- No inbound access was opened to the task.
- Used the existing execution role with `AmazonECSTaskExecutionRolePolicy`.
- Stopped the temporary Fargate task after validation to limit runtime costs.
- No public API endpoint or end-to-end remote HTTP request was validated.

## Lessons Learned
- Fargate tasks need network access to pull images and publish logs.
- Security groups, subnet routes, IAM execution roles, and log configuration all affect deployment success.
- A task reaching `RUNNING` and producing startup logs confirms deployment startup, but does not replace testing API requests against the deployed task.

## Resources
- Amazon ECR image: `cloud-engineer-web:day21`
- ECS cluster: `CloudEngineer-ECS-Cluster`
- Task definition: `day21-url-detector:1`
- CloudWatch log group: `/ecs/day21-url-detector`
