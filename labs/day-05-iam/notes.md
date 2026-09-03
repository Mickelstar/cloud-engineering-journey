# Day 5 — IAM Notes

## IAM Concepts

### IAM User
Represents a human identity that can access AWS.

### IAM Group
Groups users together so permissions can be managed consistently.

Example:
CloudEngineer-Lab
└── AdministratorAccess

### IAM Role
An identity that AWS services or workloads can assume.

Example:
EC2
└── CloudEngineer-EC2-SSM-Role

### Permissions Policy
Defines what an identity is allowed to do.

Example:
AmazonSSMManagedInstanceCore

### Trust Policy
Defines who is allowed to assume a role.

For CloudEngineer-EC2-SSM-Role:
EC2 is trusted to assume the role.

### Resource-Based Policy
A policy attached directly to a resource.

Example:
The S3 bucket policy used with CloudFront.

## Least Privilege

Give an identity only the permissions required
to perform its job.

Example:

s3:GetObject
s3:PutObject

is better than:

s3:*

or:

AdministratorAccess

when an application only needs to read and upload objects.

## Key Mental Model

Trust Policy = WHO can assume the role?

Permissions Policy = WHAT can the role do?

Resource-Based Policy = WHO/WHAT can access this resource?

## Day 5 Lab Result

Inspected:
CloudEngineer-EC2-SSM-Role

Attached policy:
AmazonSSMManagedInstanceCore

Trust relationship:
EC2 (ec2.amazonaws.com)

The EC2 instance uses the IAM role to communicate
with AWS Systems Manager without requiring inbound SSH.