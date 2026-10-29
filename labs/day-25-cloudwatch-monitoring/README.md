\# Day 25 — AWS CloudWatch Monitoring



\## Objective

Investigate CloudWatch alarm states and verify metric availability without creating resources.



\## Findings

\- `CloudEngineer-ECS-CPU-High`: State `OK`, CPU threshold 80%, 300-second period, two evaluation periods. No datapoints were received for two periods; missing data was treated as non-breaching. The state does not confirm healthy CPU utilization.

\- `CloudEngineer-Web-01-High-CPU`: State `INSUFFICIENT\_DATA`, CPU threshold 70%, 300-second period, one evaluation period.

\- EC2 instance `i-0980a6b3928003607` is stopped.

\- No EC2 CPU datapoints were returned for the inspected three-hour window.

\- EC2 detailed monitoring is disabled. Basic monitoring is separate and does not require detailed monitoring to publish CPU metrics.

\- The ECS alarm has no dimensions configured; its intended metric scope should be reviewed.



\## Lessons

\- `OK` does not always mean recent metrics confirm healthy performance.

\- `INSUFFICIENT\_DATA` can result when metrics are unavailable.

\- Check resource state and metric dimensions before changing alarms.

\- Avoid enabling monitoring or starting stopped instances unless there is a clear need.



\## Validation

\- \[x] Listed existing CloudWatch alarms.

\- \[x] Inspected thresholds, periods, dimensions, and state reasons.

\- \[x] Queried EC2 CPU statistics for the last three hours.

\- \[x] Verified the EC2 instance is stopped.



\## Cost and Safety

No resources were created, started, or modified during this investigation.



