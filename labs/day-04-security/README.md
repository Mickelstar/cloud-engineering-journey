# Day 4 — AWS Security Groups and Secure Administration

## Objective

Apply least-privilege network access to public and private EC2 workloads, and use AWS Systems Manager Session Manager instead of exposing SSH for private-instance administration.

## Security Group Configuration

### Private EC2 instance

**Security Group:** `CloudEngineer-Private-SG`

- Removed inbound SSH (TCP 22) from `0.0.0.0/0`.
- Used AWS Systems Manager Session Manager for administrative access.
- The SSM Agent initiates outbound HTTPS communication to Systems Manager; Session Manager does not require an inbound SSH rule.

### Public web server

**Security Group:** `CloudEngineer-Web-SG`

- Allowed inbound HTTP (TCP 80) from `0.0.0.0/0` for the intentionally public web server.
- This rule permits browser requests to reach the web server over HTTP.

## Traffic Model

```text
Public web server:
Internet ── HTTP / TCP 80 ──> Web Server

Private instance management:
Private EC2 ── outbound HTTPS ──> AWS Systems Manager
        (Session Manager; no inbound SSH required)
```

## Security Principles

1. Allow only the traffic a resource actually needs.
2. Avoid exposing administrative ports such as SSH to the entire internet.
3. Prefer managed access paths such as Systems Manager Session Manager for private instances.
4. Keep public application access separate from private administrative access.
5. Validate both the network rules and the instance's Systems Manager prerequisites.

## Validation Evidence

The recorded lab notes describe the Security Group rules that were removed or allowed and the reason for each decision. They do not include screenshots, rule exports, or a recorded Session Manager connection transcript.

Before treating this as a production configuration, verify:
- The instance has a suitable IAM instance profile and the required SSM permissions.
- The SSM Agent is installed and running.
- The instance can reach the Systems Manager service endpoints over HTTPS, directly or through the configured network path.
- Public HTTP is intentional; use HTTPS for production user traffic.

## Cost and Cleanup

Security Groups have no hourly charge, but EC2 and supporting networking resources may. Stop or remove lab resources when they are no longer required, while preserving any evidence needed for the portfolio.

**Day 4 status:** Security Group least-privilege decisions and the Session Manager administration approach documented.
