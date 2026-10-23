# Day 17 Notes

- ECS metrics queried: CPUUtilization, MemoryUtilization, LiveTaskCount.
- No Container Insights metrics returned for the cluster query.
- No CPU datapoints returned for the selected time window.
- Configured an 80% CPU alarm with two five-minute evaluation periods.
- Missing data behavior: `notBreaching`.
- Alarm setup verified; real threshold breach and notifications not tested.
- Check CloudWatch charges and delete the alarm when finished with the lab.
