# Day 17 — ECS Monitoring with CloudWatch

## Objective
Configure an Amazon CloudWatch metric alarm for ECS CPU utilization.

## Environment
- AWS Region: `eu-north-1`
- ECS Cluster: `CloudEngineer-ECS-Cluster`
- CloudWatch Namespace: `AWS/ECS`
- Alarm: `CloudEngineer-ECS-CPU-High`

## Implementation
- Queried available ECS metrics.
- Checked CPU utilization statistics for the selected time window.
- Found no CPU datapoints in that window.
- Created a CPU alarm with an 80% threshold, a 300-second period, and two evaluation periods.
- Configured missing data as `notBreaching`.
- Verified the alarm configuration through the AWS CLI.

## Validation and Limitations
The alarm configuration was verified, but no real CPU threshold breach was tested. The cluster had no running ECS tasks or services, and the selected time window returned no CPU datapoints. Container Insights metrics were not returned for this cluster.

## Key Lessons
- CloudWatch alarms evaluate metrics against defined thresholds.
- Missing data handling affects alarm behavior when workloads are idle.
- An alarm's existence does not prove that notifications or real incidents have been tested.
- Monitoring configuration should be validated separately from application health.

## Cost and Security
CloudWatch alarms may incur charges. Remove lab resources when no longer needed, and avoid leaving unnecessary resources active.

## Outcome
Configured and verified an ECS CPU utilization alarm without launching additional compute resources.
