# Day 20 — Lab Notes

## What I Built
A Dockerized HTTP API around the existing Python phishing URL detector.

## Security Controls
- Non-root execution using UID 10001.
- Read-only container root filesystem.
- Linux capabilities dropped.
- Privilege escalation disabled.
- Published port bound to localhost.
- Temporary filesystem mounted at `/tmp`.

## Validation
Build and runtime validation, API health check, URL analysis, and container identity checks completed successfully.

## Limitations
This is a local learning prototype, not a production service. Further work would be required for production-grade request handling, authentication, rate limiting, monitoring, image vulnerability scanning, and deployment security.

## Key Lesson
Containerization improves portability, while runtime restrictions reduce the privileges and filesystem access available to the application. Neither eliminates all container or application risks.