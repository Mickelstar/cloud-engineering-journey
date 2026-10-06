# Day 11 — Amazon ECR

## Objective

Learn how to use Amazon Elastic Container Registry (ECR) to store and manage Docker container images.

By the end of this lab:

- Create a private ECR repository
- Authenticate Docker with Amazon ECR
- Tag a local Docker image for ECR
- Push the image to ECR
- Understand the relationship between Docker, ECR, and future ECS deployments

---

## Architecture

```
Local Machine
     |
     | Docker Image
     v
Docker Engine
     |
     | docker push
     v
Amazon ECR
     |
     v
cloud-engineer-web:v1