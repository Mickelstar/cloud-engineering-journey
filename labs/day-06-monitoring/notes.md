# Day 6 — CloudWatch Monitoring Notes

## CloudWatch

CloudWatch monitors AWS resources using metrics, logs, and alarms.

## EC2 Metrics

Observed metrics for CloudEngineer-Web-01:

- CPU utilization
- Network in
- Network out
- Network packets

## CloudWatch Alarm

Alarm name:
CloudEngineer-Web-01-High-CPU

Configuration:

- Metric: CPUUtilization
- Statistic: Average
- Period: 5 minutes
- Condition: CPU > 70%
- Consecutive periods: 1

## Alarm Test

Initial state:
INSUFFICIENT_DATA

CPU load was intentionally generated to test the alarm.

The alarm entered:
ALARM

After the CPU load was stopped:
ALARM → OK

## Key Lesson

CloudWatch monitors infrastructure.

Metrics provide numbers.
Logs provide detailed records.
Alarms detect conditions and can trigger actions.

Monitoring allows engineers to detect problems instead
of discovering them only after users report them.