## Current Status

### Completed

- AWS account configured
- Billing budget and alerts configured
- IAM lab user created
- IAM MFA enabled
- S3 bucket created
- S3 versioning enabled
- S3 public access blocked
- Static website files created
- Website files uploaded to S3

### AWS Region

`eu-north-1` — Europe (Stockholm)

### Current Architecture

User → CloudFront → S3

### Security Approach

The S3 bucket remains private. CloudFront will later access the bucket using Origin Access Control (OAC).

# AWS Static Website Deployment

A production-oriented static website deployment using Amazon S3 and Amazon CloudFront.

## Architecture

```text
User
  |
  | HTTPS
  v
CloudFront
  |
  | Origin Access Control
  v
Private S3 Bucket
  |
  +-- index.html
  +-- style.css
  +-- script.js