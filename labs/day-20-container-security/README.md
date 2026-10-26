# Day 20 — Docker Containerization and Hardening

## Objective
Package the Python phishing URL detector as a Dockerized API and validate basic container security controls.

## Implementation
- Created a Python HTTP API with `/health` and `/analyze` endpoints.
- Reused the Day 18 URL detector.
- Built a Docker image based on `python:3.12-slim`.
- Ran the application as a non-root user (UID 10001).
- Bound the published port to `127.0.0.1:8080`.
- Enabled a read-only root filesystem.
- Dropped Linux capabilities and disabled privilege escalation.
- Used a temporary filesystem at `/tmp`.

## Validation
The lab's build, runtime, health-check, URL-analysis, and container-identity checks were reported successful.

Expected security checks:
- API responds on localhost.
- `/analyze` returns a risk score and explanatory reasons.
- The application runs as UID 10001 rather than root.
- Container runs with a read-only root filesystem and restricted privileges.

## Security Considerations
- The API is intended for local testing and is not production-hardened.
- The built-in Python HTTP server is a lightweight demonstration server.
- URL risk results are heuristic assessments, not proof that a URL is safe or malicious.
- No AWS deployment or public exposure was performed as part of this lab.

## Cleanup
The test container was removed after validation. The local Docker image may remain available for further testing.

## Run
Build from this directory after ensuring `detector.py` is present:

```powershell
docker build -t phishing-detector:day20 .
docker run --rm -p 127.0.0.1:8080:8080 --read-only --tmpfs /tmp --cap-drop ALL --security-opt no-new-privileges phishing-detector:day20
```

Validate the API using PowerShell requests to `/health` and `/analyze`.