\# Day 27 — AWS CloudFormation (Infrastructure as Code)



\## Objective

Create and validate an AWS CloudFormation template and inspect a proposed infrastructure change without deploying resources.



\## Template

Created `template.yaml` defining one S3 bucket with all four public-access-block settings enabled.



\## Validation

\- `aws cloudformation validate-template` succeeded.

\- Created a CloudFormation change set named `Day27-Preview`.

\- Inspected the proposed change.

\- Confirmed CloudFormation proposed adding exactly one `AWS::S3::Bucket` resource named `Day27StorageBucket`.



\## Security

The bucket template explicitly enables:

\- BlockPublicAcls

\- BlockPublicPolicy

\- IgnorePublicAcls

\- RestrictPublicBuckets



\## Cost and Safety

\- No S3 bucket was deployed.

\- The change set was deleted without execution.

\- No infrastructure resources were created.



\## Lessons

\- CloudFormation defines infrastructure declaratively using templates.

\- Template validation checks whether the template is acceptable.

\- Change sets preview proposed infrastructure changes before execution.

\- Infrastructure should be reviewed before deployment.



\## Validation Checklist

\- \[x] Created CloudFormation YAML template.

\- \[x] Validated template successfully.

\- \[x] Created a change set.

\- \[x] Verified the proposed S3 bucket resource.

\- \[x] Avoided deployment.



