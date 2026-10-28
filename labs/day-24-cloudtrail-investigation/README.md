\# Day 24 — AWS CloudTrail Investigation



\## Objective

Investigate AWS management activity using CloudTrail Event History without creating additional billable resources.



\## Environment

\- AWS Region: `eu-north-1`

\- IAM identity: `micky-cloudengineer`



\## Findings

1\. `describe-trails` returned an empty trail list in `eu-north-1`.

2\. CloudTrail Event History returned recent management events despite no trail being configured in the region.

3\. Inspected an `ec2.amazonaws.com` `DescribeNetworkInterfaces` event.

4\. The event was a read-only management API call made by the IAM user through AWS CLI on Windows.

5\. The request referenced two network interfaces.

6\. Five `ConsoleLogin` events were returned for the IAM user, dated October 7–24, 2026.



\## Security and Audit Notes

\- Event History provides recent management-event visibility without requiring a separately configured trail.

\- Login events should be inspected for outcome and context before determining whether they were successful or suspicious.

\- Raw CloudTrail events may contain account identifiers, access key IDs, IP addresses, and other sensitive metadata. Redact these before sharing publicly.

\- No trail was created and no AWS resources were modified during this investigation.



\## Limitations

This was a targeted investigation in `eu-north-1`. It does not establish that all account activity or regions were reviewed, and the five login events alone do not establish login outcomes.



\## Validation

\- \[x] Checked configured trails.

\- \[x] Retrieved recent management events.

\- \[x] Inspected a detailed EC2 API event.

\- \[x] Queried console-login events.



