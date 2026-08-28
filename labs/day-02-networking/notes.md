# Day 2 Networking Notes

## DNS

DNS translates a human-readable domain name into an IP address so the user's device can locate the requested service.

## TCP

TCP establishes reliable communication between network endpoints.

## TLS / HTTPS

TLS provides encryption and security for communication over the internet.

HTTPS uses HTTP over TLS.

## HTTP

HTTP is the application-layer protocol used for communication between clients and web servers.

## VPC

Amazon VPC provides an isolated virtual network for AWS resources.

## Subnets

Subnets divide a VPC into smaller network segments.

## Internet Gateway

An Internet Gateway allows resources in a VPC to communicate with the internet when routing and security rules permit it.

## Route Tables

Route tables determine where network traffic is directed.

## Security Groups

Security Groups control inbound and outbound traffic for supported AWS resources.

## Network ACLs

Network ACLs provide another layer of traffic control at the subnet level.

## Key Takeaway

A cloud application depends on several networking layers working together:

User → DNS → TCP/TLS → HTTPS → AWS Network → Application


# PART 9 — My Notes/Observations

```markdown
# Day 2 Notes

## DNS Observation

What did nslookup return? Non-authoritative answer: DNS request timed out.

## HTTP Observation

What status code did curl return? :It returned HTTP/1.1 200 OK

## CloudFront Observation

What did `x-cache` show? :Hit from Cloudfront

## TLS Observation

What did curl show about TLS? :SSL/TLS connection renegotiated then it confirmed with an the output(HTTP/1.1 200 OK)

## Browser Observation

What did DevTools show for index.html?

## Failed Request

What happened when I requested:

`/does-not-exist.html` :HTTP/1.1 403 Forbidden

## Troubleshooting Lesson

What layer would I investigate first when a website fails, and why?
1. DNS
   ↓
2. Network connection
   ↓
3. TLS
   ↓
4. HTTP request
   ↓
5. CloudFront
   ↓
6. Origin
   ↓
7. Object

## DNS Investigation

Command:
'nslookup dltkg6f6doi8d.cloudfront.net' :I observed and saw the server name, address,DNS request time out, Domain name and different adresses.

## CNAME Investigation

command:
'nslookup -type=CNAME dltkg6f6doi8d.cloudfront.net' :I observed and saw the cloudfront url, primary name server, responsible mail address, serial no, refresh time, retry time, expire days left and default TTL day(s) left.

## A Record Investigation

command:
'nslookup -type=A dltkg6f6doi8d.cloudfront.net' :I observed and saw the server name, address,DNS request time out, Domain name and different adresses.

## Traceroute

command:
'tracert dltkg6f6doi8d.cloudfront.net' :Network Route was traced multiple times up to 30hops

## HTTPS Investigation

command:
'curl.exe -Iv https://dltkg6f6doi8d.cloudfront.net' :A bunch of activities ranging from trying to establish connection to an IP address,get client certification,getting the 'http/1.1' approval, established connection to the cloudfront URL through the server IP and port
