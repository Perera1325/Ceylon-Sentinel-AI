# LLMOps Architecture

The LLMOps stack tracks the operational metrics of the Ceylon Sentinel AI system during every LangGraph workflow execution.

## Metrics Tracked
- **Token Usage**: Approximated tracking of context window and generation tokens.
- **Cost**: Real-time cost calculation based on token models.
- **Latency**: End-to-end execution time for the `PolicyAgent`.
- **Workflow / Agent**: Metadata tagging for which agent generated the response.

## Storage
- Employs an in-memory `LLMOpsTracker` singleton for high-performance dashboard visualization.
- Designed to integrate seamlessly with PostgreSQL via SQLAlchemy for long-term audit compliance.
