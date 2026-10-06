```
# Day 11 — Amazon ECR Notes

## 1. What is Amazon ECR?

Amazon Elastic Container Registry (ECR) is AWS's managed container registry.

It stores Docker container images so AWS services such as ECS and EKS can pull and run them.

---

## 2. Docker vs ECR

| Component | Purpose |
|---|---|
| Docker | Builds and runs containers |
| Docker Image | Package containing application + dependencies |
| ECR | Stores container images |
| ECS | Orchestrates containers |
| Fargate | Runs containers without managing servers |

Flow:

```
Application
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Amazon ECR
    ↓
ECS / Fargate