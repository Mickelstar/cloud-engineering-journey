## Security Group Failure Test

### Initial State

HTTP traffic was allowed through:

`TCP 80 → 0.0.0.0/0`

The NGINX website was accessible from the internet.

### Failure Injection

I temporarily removed the inbound HTTP port 80 rule from:

`CloudEngineer-Web-SG`

### Result

The EC2 instance remained running and NGINX remained active, but the website was no longer reachable from the browser.

### Diagnosis

The Security Group was blocking inbound HTTP traffic on TCP port 80.

### Recovery

I restored:

`HTTP → TCP → 80 → 0.0.0.0/0`

The website became accessible again.

### Lesson

A Security Group controls network traffic reaching supported AWS resources. Removing the required inbound rule can prevent external clients from reaching an application even when the application itself is running correctly.

## Internet Gateway vs NAT Gateway

### Internet Gateway

An Internet Gateway provides a path between a VPC and the internet for resources with appropriate public routing.

### NAT Gateway

A NAT Gateway allows resources in private subnets to initiate outbound internet connections without providing those resources with a direct inbound internet route.

### Architecture

Public:

Internet → Internet Gateway → Public Subnet → EC2

Private outbound:

Private EC2 → Private Route Table → NAT Gateway → Internet Gateway → Internet

### Key Lesson

A subnet is not public or private simply because of its name. Routing determines whether it has a direct path to the Internet Gateway.

## NAT Gateway Validation

A private EC2 instance was launched in CloudEngineer-Private-Subnet without a public IPv4 address.

The private subnet uses CloudEngineer-Private-RT, which contains:

0.0.0.0/0 → CloudEngineer-NAT-GW

The NAT Gateway is deployed in CloudEngineer-Public-Subnet and uses an Elastic IP.

Using AWS Systems Manager Session Manager, I verified that the private EC2 instance could successfully initiate outbound HTTPS connections to the internet.

This confirmed the following traffic path:

Private EC2
→ Private Route Table
→ NAT Gateway
→ Internet Gateway
→ Internet

The private EC2 did not require a public IPv4 address to access the internet.

## Day 3 Troubleshooting Exercise

I deliberately removed the HTTP/80 inbound rule from CloudEngineer-Web-SG.

The NGINX service remained operational on the EC2 instance, but the website became unreachable externally.

I restored the HTTP/80 rule and confirmed that the website became accessible again.

This demonstrated that Security Groups control permitted network traffic independently of whether the application itself is running.

## Day 3 Key Lessons

- A public subnet requires a route to an Internet Gateway.
- A private subnet does not have a direct route to an Internet Gateway.
- A public IPv4 address does not by itself make a subnet public.
- NAT Gateway provides outbound internet access for private resources.
- NAT Gateway is deployed in a public subnet.
- Private resources can access the internet without having public IPv4 addresses.
- Security Groups control traffic reaching supported AWS resources.
- Systems Manager can provide administrative access without exposing SSH to the internet.
- Troubleshooting should proceed layer by layer rather than changing infrastructure randomly.