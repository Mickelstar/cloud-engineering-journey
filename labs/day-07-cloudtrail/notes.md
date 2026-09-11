# Day 7 — CloudTrail Notes

## CloudTrail

AWS CloudTrail records AWS API activity for auditing.

CloudTrail helps answer:

- Who performed an action?
- What action was performed?
- When did it happen?
- Which AWS service was involved?
- What resources were affected?

## Hands-On Event

Event:
CreateSecurityGroup

User:
micky-cloudengineer

Event source:
ec2.amazonaws.com

Read-only:
false

Resources included:
- VPC
- Security Group
- CloudEngineer-Web-SG

## CloudWatch vs CloudTrail

CloudWatch:
Monitors resource health and performance using metrics,
logs, and alarms.

CloudTrail:
Records AWS API activity for auditing and investigation.

## Security Group Investigation

Useful CloudTrail events include:

AuthorizeSecurityGroupIngress
RevokeSecurityGroupIngress
AuthorizeSecurityGroupEgress
RevokeSecurityGroupEgress

## Key Lesson

CloudWatch tells us:
"How is the infrastructure doing?"

CloudTrail tells us:
"Who did what?"