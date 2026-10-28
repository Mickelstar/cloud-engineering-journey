# Day 23 — AWS Resource and Cost Hygiene

## Objective
Review AWS resources that may incur ongoing costs and identify safe cleanup opportunities.

## Checks Performed
- ECS: no running tasks and no services in CloudEngineer-ECS-Cluster.
- NAT gateways: none listed in available or pending states.
- Elastic Load Balancing: no load balancers listed.
- Elastic IPs: none listed.
- Network interfaces: two in-use ENIs identified and traced to existing EC2 instances using CloudEngineer-Web-SG and CloudEngineer-Private-SG.

## Decisions
- Did not delete the ENIs because they are attached to existing EC2 instances from earlier labs.
- No resources were deleted during this audit.

## Lessons Learned
Resource cleanup must be based on ownership and dependencies, not just whether a resource looks unused. This audit covered the listed resource types in eu-north-1; it does not prove that all AWS costs or resources have been eliminated.
