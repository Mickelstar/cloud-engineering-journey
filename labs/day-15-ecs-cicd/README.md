
# Day 15 — Automating ECS Fargate Deployment with GitHub Actions

## Objective

Extend the existing GitHub Actions CI/CD pipeline to deploy a Docker image to Amazon ECS Fargate after building and pushing the image to Amazon ECR.

## Architecture

GitHub commit
→ GitHub Actions
→ AWS authentication using OIDC
→ Docker build
→ Amazon ECR image push
→ ECS task definition revision
→ Fargate task launch
→ Task startup verification

## AWS Resources

- AWS Region: eu-north-1
- ECS Cluster: CloudEngineer-ECS-Cluster
- ECS Task Definition Family: CloudEngineer-Web-Task
- ECR Repository: cloud-engineer-web
- ECS Subnet: subnet-04e0533da95975515
- ECS Task Security Group: sg-0ec4c8cf1ba60591f
- GitHub Actions IAM Role: GitHubActions-ECR-Push

## Implementation

Updated `.github/workflows/ecr-build-push.yml` to:

1. Check out the repository.
2. Authenticate to AWS through GitHub OIDC.
3. Authenticate Docker to Amazon ECR.
4. Build the application image.
5. Push a commit-specific image tag and the `latest` tag.
6. Register a new ECS task-definition revision referencing the commit-specific image.
7. Launch an ECS Fargate task.
8. Poll ECS task status and fail the workflow if startup verification fails.

## Validation

- Confirmed the GitHub Actions workflow completed successfully.
- Confirmed the deployment steps appeared in the job logs.
- The workflow registers a new task-definition revision and launches a Fargate task.
- Startup verification checks whether the task reaches `RUNNING`.
- The task uses a public IP for outbound connectivity, but its security group does not permit public inbound HTTP.

## Security and Cost Considerations

- GitHub authenticates to AWS through OIDC rather than storing long-lived AWS access keys in GitHub.
- The deployment role requires appropriate ECS permissions and `iam:PassRole` for the task execution role.
- The task execution role needs ECR image-pull permissions.
- The task security group restricts inbound HTTP to the configured ALB security group.
- A public IP does not make the application publicly accessible when inbound HTTP is blocked.
- Fargate tasks incur charges while running. Stop test tasks after validation.
- CloudWatch logging is configured in the ECS task definition.

## Lessons Learned

- A successful Docker build does not prove that deployment succeeded.
- Task-definition revisions provide a record of the image configuration used for deployment.
- Commit-specific image tags improve traceability and rollback investigations.
- CI/CD deployment validation should check the actual ECS task status.
- IAM permissions and network connectivity are both critical to successful deployments.

## Outcome

Implemented and verified a GitHub Actions workflow that builds and pushes a container image and automates ECS Fargate task deployment and startup verification.
