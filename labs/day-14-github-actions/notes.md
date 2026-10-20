# Day 14 — Lab Notes

## Key configuration

- Workflow: `.github/workflows/ecr-build-push.yml`
- Application and Dockerfile: `labs/apps/cloud-engineer-web/`
- AWS region: `eu-north-1`
- ECR repository: `cloud-engineer-web`
- IAM role: `GitHubActions-ECR-Push`
- Authentication: GitHub Actions OIDC
- Trigger: pushes to `main` affecting the application or workflow files, plus manual workflow dispatch

## Problems encountered and fixes

### 1. OIDC role assumption denied

**Error:** `Not authorized to perform sts:AssumeRoleWithWebIdentity`

**Cause:** The IAM trust policy's subject did not match the immutable subject format GitHub issued for this repository.

**Fix:** Updated the role trust policy to match the actual GitHub OIDC subject and retained the `sts.amazonaws.com` audience condition.

### 2. Incorrect Docker build context

**Problem:** The workflow referenced a path that did not exist.

**Fix:** Set the build context to `./labs/apps/cloud-engineer-web` and aligned the workflow path filter with the actual application location.

### 3. Missing ECR permission

**Error:** The role was denied `ecr:BatchGetImage`.

**Fix:** Updated the repository-scoped ECR permissions to include the required image retrieval and publishing actions.

### 4. GitHub Actions queue delay

**Problem:** A GitHub Actions service incident delayed workflow processing.

**Resolution:** Waited for the platform to recover and continued checking the workflow instead of making unrelated infrastructure changes.

## Verification checklist

- [x] Docker build completed.
- [x] Image tag `latest` exists in ECR.
- [x] Image tag `4ea6a06e1eb90de3c2d8f5293775b55c08505a90` exists in ECR.
- [x] Both tags verified in the ECR console.
- [ ] Review and update deprecated GitHub Actions runtimes in a separate maintenance change.

## Main takeaway

A reliable CI/CD pipeline requires correct source paths, trusted identity federation, least-privilege IAM permissions, and verification of the artifact in the destination registry—not merely a successful Docker build.
