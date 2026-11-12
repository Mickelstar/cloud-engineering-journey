# Day 1 — Application Audit and Baseline Validation

## Objective

Audit the existing URL Detector application, establish a working Docker baseline, validate its API, and improve request validation before preparing it for AWS deployment.

## Existing Application

The application is a Python-based URL risk detector.

**Location:** `labs/day-20-container-security/`

Key components:
- `app.py` — HTTP API.
- `detector.py` — URL risk-scoring logic.
- `Dockerfile` — Container image definition.

The detector uses heuristic checks to assign risk scores and classify URLs. Its results are indicative, not definitive proof that a URL is malicious.

## Work Completed

### 1. Application audit
- Located and inspected the existing application.
- Reviewed its API routes, input handling, and detector integration.
- Identified opportunities to improve request validation.

### 2. Baseline testing
- Executed the existing Python unit test suite.
- Confirmed all 8 detector tests passed.

### 3. Docker validation
- Built the application image:
  `url-detector:capstone-baseline`
- Started the container:
  `url-detector-capstone`
- Confirmed the application was running on port 8080.

### 4. API validation

Verified:
- `GET /health` returned HTTP 200.
- Unknown GET endpoint returned HTTP 404.
- Valid HTTPS URL returned HTTP 200.
- Empty URL returned HTTP 400 after the improvement.
- Invalid JSON structure returned HTTP 400.
- Malformed JSON returned HTTP 400.

### 5. API improvements

Updated `app.py` to:
- Validate that incoming JSON is an object.
- Reject empty URL values.
- Return HTTP 400 for URLs classified as invalid.
- Include a content length in the health response.

## Validation Results

| Check | Result |
|---|---|
| Existing unit tests | 8 passed |
| Docker image build | Successful |
| Container startup | Successful |
| Health endpoint | Passed |
| Unknown endpoint | HTTP 404 |
| Valid URL request | HTTP 200 |
| Empty URL request | HTTP 400 |
| Invalid JSON structure | HTTP 400 |
| Malformed JSON | HTTP 400 |

## Lessons Learned

1. A successful container build does not prove that an application behaves correctly.
2. API input validation is essential for predictable error handling.
3. Health endpoints provide a basic mechanism for checking application availability.
4. Existing unit tests should be rerun after application changes.
5. Docker provides a reproducible environment for packaging and running the application.

## Current Limitations

- The API still uses Python's built-in `HTTPServer`.
- No production application server has been introduced.
- No AWS infrastructure has been provisioned.
- No automated CI/CD pipeline has been configured.
- The application has not yet been deployed to ECS.

## Next Steps

- Improve application robustness and test coverage.
- Prepare the application for production container deployment.
- Design the AWS networking and infrastructure architecture.
- Introduce Terraform and ECS Fargate in subsequent capstone stages.

**Day 1 status:** Application audit, baseline testing, Docker build, and API validation completed.