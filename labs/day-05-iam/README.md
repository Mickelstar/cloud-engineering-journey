# Day 5 — IAM & Access Control

## Objective

Understand AWS identity, roles, policies, trust relationships,
and the principle of least privilege.

## What I Learned

- IAM users represent human identities.
- IAM groups organize users and permissions.
- IAM roles provide identities for AWS workloads.
- Trust policies define who can assume a role.
- Permissions policies define what a role can do.
- Resource-based policies are attached directly to resources.
- Least privilege means granting only required permissions.

## Hands-On

Inspected:

CloudEngineer-EC2-SSM-Role

Policy:

AmazonSSMManagedInstanceCore

Trust:

EC2 is trusted to assume the role.

## Architecture

EC2
↓
IAM Role
↓
AmazonSSMManagedInstanceCore
↓
AWS Systems Manager

## Key Lesson

Humans use identities.

AWS workloads should generally use IAM roles
instead of personal credentials.