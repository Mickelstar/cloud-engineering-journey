\# Day 26 — AWS Systems Manager Investigation



\## Objective

Audit AWS Systems Manager configuration and EC2 management readiness without starting instances or creating resources.



\## Findings

\- No managed EC2 instances were returned by `ssm describe-instance-information`.

\- Two EC2 instances were identified:

&#x20; - CloudEngineer-Private-01 (`i-0076ef9bd7c9cc425`) — stopped.

&#x20; - CloudEngineer-Web-01 (`i-0980a6b3928003607`) — stopped.

\- Both instances have the `CloudEngineer-EC2-SSM-Role` instance profile attached.

\- The role has `AmazonSSMManagedInstanceCore` attached.

\- No association records were returned for the web instance.

\- No hybrid activations were returned.



\## Lessons

\- An attached IAM role is necessary but does not prove an instance is registered with Systems Manager.

\- SSM Agent availability, network connectivity, instance state, and IAM permissions all affect SSM management.

\- Stopped instances cannot provide current agent connectivity or registration evidence.



\## Limitations

SSM Agent installation and runtime health were not verified. Both instances remained stopped, and no resources were started or modified.



\## Validation

\- \[x] Queried SSM managed instances.

\- \[x] Inspected EC2 instance states and instance profiles.

\- \[x] Verified the SSM managed policy.

\- \[x] Queried instance association status.

\- \[x] Checked hybrid activations.



