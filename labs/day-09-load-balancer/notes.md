# Day 9 Notes — Application Load Balancer

## What I Learned

### Application Load Balancer

An ALB provides a public entry point for HTTP/HTTPS applications and forwards requests to registered targets.

### Target Group

The target group contains the backend resources that receive traffic from the ALB.

In this lab:

```text
CloudEngineer-Web-TG
        |
        v
CloudEngineer-Web-01

### Resources Created

Application Load Balancer
Name: CloudEngineer-ALB
Type: Application Load Balancer
Scheme: Internet-facing
IP type: IPv4
Listener: HTTP :80
Default action: Forward to CloudEngineer-Web-TG
Security group: CloudEngineer-ALB-SG
ALB Security Group
Name: CloudEngineer-ALB-SG
Inbound:
HTTP TCP 80 from 0.0.0.0/0
Outbound:
Default outbound access
Target Group
Name: CloudEngineer-Web-TG
Target type: Instances
Protocol: HTTP
Port: 80
Health check path: /
Registered target: CloudEngineer-Web-01
EC2 Web Server
Name: CloudEngineer-Web-01
Web server: NGINX
HTTP port: 80
Security group: CloudEngineer-Web-SG

Key Lessons
1. An ALB distributes incoming application traffic to registered targets.
2. A target group defines which resources receive ALB traffic.
3. ALB health checks determine whether targets are healthy.
4. Security groups can reference another security group as the traffic source.
5. Security-group chaining allows the EC2 server to trust only the ALB.
6. A public EC2 instance can still be protected from direct application traffic using security-group rules.
7. The ALB becomes the controlled public entry point for the application.

Day 9 Outcome

Successfully deployed and tested an internet-facing Application Load Balancer with:

1. Target group
2. Health checks
3. HTTP listener
4. ALB security group
5. EC2 security-group chaining
6. Direct-access protection
```