# Day 22 — AWS IAM Least-Privilege Audit

## Objective
Review IAM user and role permissions used by the cloud engineering environment without modifying production permissions.

## Audit Findings
- IAM user `micky-cloudengineer` has the attached managed policy `IAMUserChangePassword`.
- `ecsTaskExecutionRole` has `AmazonECSTaskExecutionRolePolicy`, with no inline policies.
- `GitHubActions-ECR-Push` has two inline policies:
  - ECR authorization uses `ecr:GetAuthorizationToken` with `Resource: "*"`.
  - Image push operations are scoped to the `cloud-engineer-web` repository in `eu-north-1`.
  - ECS task actions (`DescribeTaskDefinition`, `RegisterTaskDefinition`, `RunTask`, `DescribeTasks`) use `Resource: "*"`.
  - `iam:PassRole` is scoped to `ecsTaskExecutionRole`.

## Security Assessment
- Positive: ECR image operations are restricted to a specific repository.
- Positive: `iam:PassRole` is limited to the ECS execution role.
- Improvement opportunity: review whether ECS actions can be scoped to specific task definitions and clusters where supported.
- Review the GitHub Actions trust policy and restrict who or what repository/workflow can assume the role.
- This audit inspected attached and inline policies; it did not establish effective permissions from every possible policy source.

## Changes
No IAM permissions were changed during this audit.

## Lessons Learned
Least privilege requires reviewing both managed and inline policies, resource scopes, role trust relationships, and the actions a workflow actually needs.
