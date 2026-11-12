# Day 3 — VPC Networking and Connectivity

## Objective

Understand how VPC routing, Internet Gateways, NAT Gateways, and Security Groups affect connectivity to public and private AWS resources.

## What This Lab Covers

- Public and private subnet routing
- Internet Gateway (IGW) connectivity
- NAT Gateway outbound connectivity
- Security Group ingress controls
- Troubleshooting network access independently of application health
- Session Manager access without exposing SSH

## Network Paths

### Public workload

A public subnet uses a route to an Internet Gateway. An internet-facing EC2 instance also needs an appropriate public IPv4 address and Security Group rules.

```text
Internet
   |
Internet Gateway
   |
Public Subnet / Route Table
   |
EC2 web server
```

### Private workload — outbound access

A private subnet can send outbound internet traffic through a NAT Gateway located in a public subnet. The private instance does not need a public IPv4 address.

```text
Private EC2
   |
Private Route Table
   | 0.0.0.0/0
NAT Gateway (public subnet, Elastic IP)
   |
Internet Gateway
   |
Internet
```

A subnet is not public or private because of its name. Its route table and the resource's addressing and security configuration determine its connectivity.

## Hands-on Validation

### 1. Security Group failure injection

**Security Group:** `CloudEngineer-Web-SG`

1. Confirmed that inbound HTTP on TCP port 80 from `0.0.0.0/0` allowed the NGINX website to load.
2. Temporarily removed the inbound HTTP rule.
3. Confirmed that the EC2 instance and NGINX remained running while the website became unreachable from the browser.
4. Restored the HTTP/80 rule and confirmed that browser access returned.

**Finding:** The application can remain healthy while network policy prevents clients from reaching it. Diagnose the application and network layers separately.

### 2. NAT Gateway validation

The private EC2 instance was launched in `CloudEngineer-Private-Subnet` without a public IPv4 address. Its route table, `CloudEngineer-Private-RT`, included:

```text
0.0.0.0/0 → CloudEngineer-NAT-GW
```

The NAT Gateway was deployed in `CloudEngineer-Public-Subnet` and associated with an Elastic IP. Using AWS Systems Manager Session Manager, outbound HTTPS connectivity from the private instance was verified.

**Finding:** Private instances can initiate outbound internet connections through NAT without being directly addressable from the internet.

## Key Lessons

- A public subnet needs a route to an Internet Gateway; internet-facing instances also need suitable addressing and security rules.
- A private subnet does not use a direct default route to an Internet Gateway.
- A NAT Gateway is placed in a public subnet and provides outbound connectivity for private resources.
- Security Groups control permitted traffic independently of application process health.
- Session Manager can provide administrative access without opening inbound SSH.
- Troubleshoot layer by layer instead of changing multiple network settings at once.

## Evidence and Scope

The results above reflect the lab notes recorded for this exercise. The notes document the connectivity tests and observed recovery; they do not include exported VPC configuration, route-table screenshots, or infrastructure-as-code.

## Further Improvements

- Add a VPC diagram and sanitized route-table evidence.
- Record subnet CIDRs, Availability Zones, route-table associations, and Security Group rules.
- Capture the exact outbound HTTPS test command and result.
- Review NAT Gateway hourly and data-processing charges; remove lab resources when they are no longer needed.

**Day 3 status:** Networking concepts, NAT outbound connectivity, and Security Group failure/recovery exercises documented.
