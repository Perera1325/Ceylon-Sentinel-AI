# Explainable AI (XAI)

The Explainable AI module guarantees transparency for every decision made by the Ceylon Sentinel AI platform.

## Output Schema
Defined in `app/ai/models/explainability.py`, every output must adhere to the `ExplainableReport` format, containing:
1. **Summary**: Clear executive decision.
2. **Evidence**: List of sources (Weather, News, RAG) used to reach the conclusion.
3. **Confidence**: 0.0 to 1.0 confidence score.
4. **Limitations**: Any missing data or uncertainties.
5. **Recommendations**: Actionable next steps.
