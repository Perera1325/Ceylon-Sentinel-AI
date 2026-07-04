# Evaluation Framework

The Evaluation Framework ensures that AI outputs meet enterprise quality standards before being delivered to the dashboard.

## Key Metrics
1. **Groundedness**: Measures how strictly the AI adheres to the facts presented in the retrieved RAG documents.
2. **Hallucination Risk**: Inversely proportional to Groundedness. High values flag unsupported statements.
3. **Completeness**: Evaluates if the response contains sufficient detail to form an actionable policy recommendation.

## Implementation
Located in `app/ai/evaluation/evaluator.py`, the `EvaluationFramework` and `HallucinationDetector` classes provide the heuristics (and future LLM-as-a-judge pipelines) to score responses.
