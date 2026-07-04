# Enterprise Operations Manual

## System Monitoring & Observability
- **Metrics Endpoint**: `/api/v1/metrics` exposes Prometheus metrics.
- **Logging**: Application logs are output in JSON format (via `pythonjsonlogger`) to standard output (stdout), allowing easy ingestion by Fluentd, Logstash, or Datadog.

## Administrative Dashboard
The Admin Dashboard (`/admin`) is the primary interface for system operators.
- **User Directory**: Provision and disable user accounts, modify RBAC roles.
- **LLMOps**: Audit token usage, inspect hallucinations, and tweak system prompt instructions dynamically.

## Troubleshooting
- **Pod CrashloopBackOff**: Inspect logs via `kubectl logs <pod-name> -n ceylon-sentinel`. Usually indicates missing Secrets/ConfigMaps or database connection issues.
- **High Latency**: Inspect the `LLMOpsTracker` telemetry. If API Latency is normal but Agent Latency is high, the upstream LLM provider is throttling requests. Consider failing over to the backup LLM provider.
