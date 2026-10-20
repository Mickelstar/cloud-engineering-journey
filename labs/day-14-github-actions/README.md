# Day 14 — CI/CD with GitHub Actions and Amazon ECR

## Objective

Automate Docker image builds and publishing to Amazon Elastic Container Registry (ECR) whenever relevant application or workflow files change on the `main` branch.

## Architecture

GitHub repository → GitHub Actions → AWS IAM via OIDC → Amazon ECR

## What I built

- Created a GitHub Actions workflow to build and publish a Docker image.
- Configured AWS authentication using OpenID Connect (OIDC), avoiding long-lived AWS access keys stored in GitHub Secrets.
- Created and configured the `GitHubActions-ECR-Push` IAM role and its ECR permissions.
- Configured the Docker build context to `labs/apps/cloud-engineer-web`.
- Published the image to ECR with two tags:
  - `latest`
  - `4ea6a06e1eb90de3c2d8f5293775b55c08505a90`

## AWS Configuration

- **Region:** `eu-north-1`
- **AWS account:** `483997780704`
- **ECR repository:** `cloud-engineer-web`
- **Image URI:** `483997780704.dkr.ecr.eu-north-1.amazonaws.com/cloud-engineer-web`

## Validation

- Confirmed the Docker build completed successfully in GitHub Actions.
- Confirmed both `latest` and commit-SHA tags appeared in the ECR repository.
- Resolved an OIDC role-assumption issue by aligning the IAM trust policy with the repository's actual GitHub OIDC subject.
- Corrected the ECR permissions after identifying a missing `ecr:BatchGetImage` authorization.
- Verified the published image tags in the ECR console.

## Security and operational lessons

- OIDC provides short-lived AWS credentials without requiring long-lived AWS access keys in GitHub Secrets.
- The IAM trust policy must match the GitHub token's subject and audience claims.
- IAM permissions must cover the ECR operations required by the publishing workflow.
- Successful image building and successful image publishing are separate checks; verify the resulting tags in ECR.
- GitHub Actions reported Node.js runtime deprecation and runner-image migration notices. These are maintenance items to review separately.

## Result

The GitHub Actions pipeline successfully built and published the application image to Amazon ECR. Both expected image tags were verified.

## Cleanup and cost

No ECS service or compute deployment was created as part of this lab. Review ECR storage and remove unused images when they are no longer needed.
