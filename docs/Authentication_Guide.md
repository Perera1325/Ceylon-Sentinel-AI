# Authentication & RBAC Guide

Ceylon Sentinel AI implements a robust, stateless JWT-based authentication system suitable for distributed enterprise deployments.

## Architecture
- **Protocol**: OAuth2 Password Flow with Bearer Tokens.
- **Hashing**: Argon2 / Bcrypt via `passlib`.
- **Stateless Tokens**: JWT encoded with `HS256`.

## Role-Based Access Control (RBAC)
Four primary roles dictate authorization levels across the system:
1. **Administrator**: Full system access, LLMOps configuration, and user management.
2. **Emergency Operator**: Can trigger early-warning broadcasts and view high-level risk dashboards.
3. **Analyst**: Has read access to historical vector databases, raw telemetry, and AI reporting.
4. **Public User**: Can view sanitized public-facing dashboards without accessing sensitive intel.

## Endpoints
- `POST /api/v1/auth/login`: Exchanges email/password for an `access_token`.
- `GET /api/v1/auth/me`: Validates token and returns current user profile.

*(Note: Production systems must rotate `SECRET_KEY` frequently using Vault or AWS KMS)*.
