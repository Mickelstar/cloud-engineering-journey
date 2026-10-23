# Day 16 — Centralized Logging with Amazon CloudWatch

## Objective
Inspect ECS container logs in Amazon CloudWatch and configure log retention to control unnecessary long-term storage.

## Environment
- AWS Region: `eu-north-1`
- ECS Task Family: `CloudEngineer-Web-Task`
- CloudWatch Log Group: `/ecs/CloudEngineer-Web-Task`
- Log Stream Prefix: `ecs`

## Implementation
- Retrieved container log events using the AWS CLI.
- Confirmed NGINX lifecycle messages were available in CloudWatch.
- Configured the log group to retain logs for 14 days.
- Verified the retention setting using `describe-log-groups`.

## Validation Results
- Log retrieval: Successful.
- Retention policy: 14 days confirmed.
- Stored bytes at verification: 13,055.

The retrieved events included NGINX graceful-shutdown and worker-process exit messages. These indicate a container shutdown sequence; they do not, by themselves, establish the cause of the shutdown.

## Key Lessons
- Centralized logs help investigate container behavior without accessing the container directly.
- Log streams organize events from individual container instances.
- Retention policies help manage log lifecycle and storage costs.
- Logs must be interpreted alongside ECS task status and application health.

## Cost and Security Notes
- A 14-day retention policy limits how long events remain available; it does not eliminate all CloudWatch charges.
- Review log ingestion and storage costs as usage grows.
- Avoid placing secrets or sensitive data in application logs.

## Outcome
Validated ECS container log retrieval and configured a 14-day CloudWatch log retention policy.
