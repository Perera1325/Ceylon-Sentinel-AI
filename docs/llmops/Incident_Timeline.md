# Incident Timeline

The Incident Timeline provides a chronological view of events leading up to an AI decision.

## Process
1. Extracted dynamically from `PolicyAgent` sub-agents.
2. Temporal entities (timestamps, events, source names) are collected.
3. Formatted into a chronological list.
4. Exposed via `GET /api/v1/intelligence/timeline`.
5. Visualized on the Dashboard in real-time.
