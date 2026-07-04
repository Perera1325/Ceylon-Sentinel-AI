# Enterprise Security Guide

Security is a primary consideration in Ceylon Sentinel AI, operating on a Zero-Trust architecture.

## API Security layer
The FastAPI application (`app/main.py`) implements the following strict middleware:
- **CORS**: Strict Origin controls (restricted to explicitly configured frontend domains).
- **Security Headers**: Injects `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, and `X-XSS-Protection`.
- **JWT Middleware**: Validates structural and cryptographic integrity of access tokens.

## Cloud & Container Security
- **Least Privilege**: Docker containers run as non-root `appuser` (UID 999).
- **Vulnerability Scanning**: Automated Trivy vulnerability scans are run in GitHub Actions on every Pull Request.
- **Dependency Audit**: Handled via Dependabot + manual CI step.

## Rate Limiting (Mocked)
In production, a Redis-backed rate limiter is attached to the API gateway to prevent DDoS and API-exhaustion attacks against the LLM providers.
