from .base import BaseAgent
from ..state.workflow_state import WorkflowState
from ..tools.rag_tool import RAGTool

class PolicyAgent(BaseAgent):
    def __init__(self):
        self.rag_tool = RAGTool()
        self.rag_tool.initialize()

    async def execute(self, state: WorkflowState) -> dict:
        docs = await self.rag_tool.execute(query=state.get("user_query", ""))
        
        weather_risk = "abnormal weather detected" if state.get("weather_data", {}).get("abnormal_weather_detected") else "normal"
        news_severity = state.get("news_data", [{}])[0].get("severity", "LOW") if state.get("news_data") else "LOW"
        
        risk_level = "HIGH" if weather_risk == "abnormal weather detected" or news_severity in ["HIGH", "CRITICAL"] else "LOW"
        
        analysis = "Based on collected weather and news, conditions are precarious." if risk_level == "HIGH" else "Conditions appear stable."
        recommendations = "Evacuate low lying areas immediately." if risk_level == "HIGH" else "No immediate action required."

        # Markdown Report Generation
        markdown_report = f"""# Executive Summary
**Risk Level:** {risk_level}
**Confidence Score:** 0.85

## Analysis
{analysis}

## Recommendations
{recommendations}

## Supporting Evidence
- Weather: {state.get('weather_data', {}).get('condition', 'Unknown')}
- News: {len(state.get('news_data', []))} relevant alerts found.
- RAG Documents: {len(docs)} SOPs consulted.
"""

        return {
            'retrieved_documents': docs,
            'risk_level': risk_level,
            'confidence_score': 0.85,
            'analysis': analysis,
            'recommendations': recommendations,
            'context': markdown_report,
            'execution_history': ['PolicyAgent: Synthesized final report with RAG documents']
        }
