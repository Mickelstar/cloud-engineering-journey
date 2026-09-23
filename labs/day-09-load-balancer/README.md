# Day 9 — Application Load Balancer

## Objective

Deploy an AWS Application Load Balancer(ALB) in front of an EC2 web server and configure security-group chaining so the EC2 instance accepts HTTP traffic only from the ALB.

---

## Architecture

```text
Internet
   |
   | HTTP :80
   v
Application Load Balancer
CloudEngineer-ALB
   |
   | HTTP :80
   v
Target Group
CloudEngineer-Web-TG
   |
   v
EC2
CloudEngineer-Web-01
   |
   v
NGINX