
# Day 15 Notes — ECS Fargate CI/CD

## Key Concepts

### Continuous Integration
GitHub Actions builds the Docker image and pushes it to Amazon ECR.

### Continuous Deployment
The workflow registers a new ECS task-definition revision and launches a Fargate task.

### AWS OIDC
GitHub Actions assumes an AWS IAM role using OIDC, avoiding long-lived AWS credentials stored as repository secrets.

### Image Versioning
The workflow publishes:
- A commit-specific image tag using `${{ github.sha }}`
- A `latest` tag

The commit-specific tag makes deployments easier to trace to source code.

### ECS Task Definition
A task definition describes the container image, CPU, memory, networking mode, execution role, and other runtime settings.

### Deployment Verification
The workflow polls ECS task status and reports failure if the task stops before reaching `RUNNING` or does not reach that state within the timeout.

## Troubleshooting Lessons

- ECR push permissions and ECS deployment permissions are separate concerns.
- `iam:PassRole` is required to pass the ECS task execution role when registering a task definition.
- Fargate tasks need working network connectivity to pull images from ECR.
- A task reaching `RUNNING` confirms startup, not end-to-end application health.
- A public IP alone does not permit inbound traffic; security-group rules still apply.

## Cost Awareness

Stop temporary Fargate tasks after testing. Avoid leaving load balancers or other billable resources running when they are not needed.

## Validation Status

GitHub Actions workflow: successful.
ECR build and push: successful.
ECS deployment steps: present and completed successfully according to the workflow run.

Public HTTP accessibility: not verified.
