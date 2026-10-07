# Day 12 — Amazon ECS + Fargate

## Objective

Deploy the Docker image stored in Amazon ECR as a running container using Amazon ECS and AWS Fargate.

---

## Architecture

```text
Docker Image
     ↓
Amazon ECR
     ↓
ECS Task Definition
     ↓
ECS Cluster
     ↓
AWS Fargate
     ↓
Running Container
     ↓
Public IP
     ↓
Browser