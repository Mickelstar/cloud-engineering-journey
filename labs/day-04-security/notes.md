# Day 4 — Security Notes

## Security Group Testing

### Private Server

Security Group:
CloudEngineer-Private-SG

Removed:
SSH | TCP | 22 | 0.0.0.0/0

Reason:
The private EC2 instance does not need inbound SSH access.
AWS Systems Manager Session Manager is used for management instead.

SSM continues to work because the SSM Agent initiates outbound
HTTPS communication to AWS Systems Manager.

### Public Web Server

Security Group:
CloudEngineer-Web-SG

Allowed:
HTTP | TCP | 80 | 0.0.0.0/0

Reason:
The web server is intentionally public and needs to receive
HTTP requests from internet users.

## Security Lesson

Public server:
Internet → HTTP → Web Server

Private server:
Private Server → Outbound HTTPS → AWS Systems Manager

Key principle:
Only allow the traffic that a resource actually needs.