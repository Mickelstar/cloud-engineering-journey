# 1. Starting Architecture

The private EC2 instance was configured as:

- Instance: `CloudEngineer-Private-01`
- VPC: `CloudEngineer-VPC`
- Subnet: `CloudEngineer-Private-Subnet`
- Security Group: `CloudEngineer-Private-SG`
- IAM Role: `CloudEngineer-EC2-SSM-Role`
- Public IPv4: None

The IAM role contains:

`AmazonSSMManagedInstanceCore`

This allows the EC2 instance to communicate with AWS Systems Manager.


# 2. Cost Optimization

During the previous lab, a NAT Gateway was used to provide outbound internet access to the private subnet.

The NAT Gateway was later deleted because it was generating unnecessary recurring costs while the lab was not actively being used.

The private route table was also cleaned up.

The final private route table contains the local VPC route without a NAT Gateway default route.

This means the private subnet no longer has general outbound internet access.



# 3. Initial SSM Test

After starting `CloudEngineer-Private-01`, the instance initially appeared in Systems Manager.

The managed node eventually showed:

`Lost connection`

Starting a Session Manager terminal also failed with:

`i-0076ef9bd7c9cc425 is not connected`

This happened because the private EC2 instance no longer had a network path to the Systems Manager service after the NAT Gateway was removed.

# 4. Solution — VPC Interface Endpoints

Instead of recreating the NAT Gateway, VPC interface endpoints were created.

Three endpoints were configured:

com.amazonaws.eu-north-1.ssm
com.amazonaws.eu-north-1.ssmmessages
com.amazonaws.eu-north-1.ec2messages

FINAL ARCHITECTURE

                 AWS VPC
┌──────────────────────────────────────────────┐
│                                              │
│   Private Subnet                             │
│                                              │
│   ┌──────────────────────┐                   │
│   │ CloudEngineer-       │                   │
│   │ Private-01           │                   │
│   │                      │                   │
│   │ No Public IP         │                   │
│   │ No SSH               │                   │
│   └──────────┬───────────┘                   │
│              │ HTTPS 443                     │
│              ▼                               │
│   ┌──────────────────────────────┐           │
│   │ VPC Interface Endpoints      │           │
│   │                              │           │
│   │ SSM                          │           │
│   │ SSM Messages                 │           │
│   │ EC2 Messages                 │           │
│   └──────────────┬───────────────┘           │
│                  │                            │
└──────────────────┼────────────────────────────┘
                   ▼
          AWS Systems Manager
                   │
                   ▼
          Session Manager