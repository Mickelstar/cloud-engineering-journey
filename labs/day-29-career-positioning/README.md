# Day 29 - Career Positioning & Technical Portfolio Review

## Objective

Translate the 30-day cloud engineering challenge into clear, evidence-based project experience suitable for recruiters and technical interviews.

## Core Technical Experience

### 1. AWS Infrastructure & Operations
- Audited AWS resources and configurations across multiple services.
- Reviewed IAM users, roles, managed policies, and inline permissions.
- Inspected EC2 instance profiles and Systems Manager configuration.
- Reviewed CloudWatch alarms and investigated missing metric data.
- Examined CloudTrail Event History to understand recorded AWS API activity.

### 2. Infrastructure as Code
- Created and validated an AWS CloudFormation template.
- Generated and reviewed a change set.
- Confirmed the proposed resource change before deployment.
- Deleted the change set without executing it.

### 3. Containers & Deployment
- Built and pushed a container image to Amazon ECR.
- Configured an ECS Fargate task using a non-root container user.
- Verified task startup and application logs in CloudWatch.
- Stopped the task after validation.

### 4. Security & Cost Awareness
- Reviewed IAM permissions and resource scope.
- Inspected AWS resources for potential ongoing costs.
- Avoided deleting resources without confirming ownership and dependencies.
- Distinguished missing monitoring data from confirmed service health.

## Interview Project Stories

### Story 1 - CloudFormation Change-Set Review

**Situation:** I needed to practise infrastructure deployment safely.

**Action:** I created a CloudFormation template, validated it, and generated a change set.

**Result:** The change set showed one proposed S3 bucket addition. I reviewed it and deleted the change set without deploying the resource.

### Story 2 - CloudWatch Monitoring Investigation

**Situation:** Existing CloudWatch alarms showed different states.

**Action:** I inspected alarm configurations, thresholds, dimensions, and available metric data.

**Result:** I identified missing metric data and documented why an `OK` alarm state did not necessarily confirm healthy application performance.

### Story 3 - ECS Fargate Deployment

**Situation:** I wanted to validate a containerized application in AWS.

**Action:** I pushed the image to ECR and ran an ECS Fargate task configured with a non-root user.

**Result:** The task reached `RUNNING`, and CloudWatch Logs confirmed that the application started listening on port 8080. I stopped the task after validation.

## Important Lessons

- Validate infrastructure changes before execution.
- Apply least-privilege principles to IAM permissions.
- Treat missing monitoring data as an observability gap, not proof of health.
- Consider cost and resource dependencies before cleanup.
- Document what was tested, what succeeded, and what remains unverified.

## Evidence & Portfolio

GitHub repository: https://github.com/Mickelstar/cloud-engineering-journey

Key project documentation:

- [Day 21 - ECS Deployment](../day-21-ecs-deployment/README.md)
- [Day 22 - IAM Audit](../day-22-iam-audit/README.md)
- [Day 23 - Cost Hygiene](../day-23-cost-hygiene/README.md)
- [Day 24 - CloudTrail Investigation](../day-24-cloudtrail-investigation/README.md)
- [Day 25 - CloudWatch Monitoring](../day-25-cloudwatch-monitoring/README.md)
- [Day 26 - Systems Manager](../day-26-systems-manager/README.md)
- [Day 27 - CloudFormation](../day-27-cloudformation/README.md)

## Day 29 Outcome

Created an evidence-based summary of practical cloud engineering work, technical problem-solving, validation, security awareness, and operational lessons for career positioning and interview preparation.
