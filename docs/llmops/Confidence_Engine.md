# Confidence Engine

The Confidence Engine computes the reliability of the final AI decision.

## Calculation
- **Tool Success (40%)**: Did the Weather API and News Crawler successfully return data?
- **RAG Context (30%)**: Did the vector database return relevant historical policies?
- **LLM Certainty (30%)**: Inferred from model logprobs (or set statically based on model config).

The resulting 0.0 to 1.0 score is surfaced to the dashboard and embedded in Explainable AI reports.
