# Risk Engine

The Risk Engine is a deterministic heuristic service that fuses unstructured and structured data into a unified Risk Score (0-100).

## Scoring Matrix
- **Weather Severity (50pts)**: Based on anomaly scores and alerts from the WeatherAgent.
- **News Severity (30pts)**: Based on keyword matching (flood, cyclone, critical) and sentiment analysis from the NewsAgent.
- **Context Depth (20pts)**: Based on the relevance and volume of retrieved historical SOPs from the RAG Vector DB.

## Risk Levels
- 0-30: **Low**
- 31-60: **Medium**
- 61-85: **High**
- 86-100: **Critical**
