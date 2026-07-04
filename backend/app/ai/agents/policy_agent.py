from .base import BaseAgent
from ..state.workflow_state import WorkflowState
from ..tools.rag_tool import RAGTool
from ..services.risk_engine import RiskEngine
from ..services.confidence_engine import ConfidenceEngine
from ..services.reporting import ExecutiveReporting
from ..telemetry.llmops import LLMOpsTracker
import time

class PolicyAgent(BaseAgent):
    def __init__(self):
        self.rag_tool = RAGTool()
        self.rag_tool.initialize()

    async def execute(self, state: WorkflowState) -> dict:
        start_time = time.time()
        
        # 1. Retrieve Context
        docs = await self.rag_tool.execute(query=state.get("user_query", ""))
        
        weather_data = state.get("weather_data", {})
        news_data = state.get("news_data", [])
        
        # 2. Risk Engine
        risk_result = RiskEngine.calculate_risk(weather_data, news_data, docs)
        risk_level = risk_result["level"]
        
        # 3. Confidence Engine
        weather_success = bool(weather_data)
        news_success = len(news_data) > 0
        confidence_score = ConfidenceEngine.calculate_confidence(weather_success, news_success, len(docs), llm_certainty=0.9)
        
        # 4. Generate Explainable Report Data
        analysis = "Based on collected weather and news, conditions are precarious." if risk_level in ["High", "Critical"] else "Conditions appear stable."
        recommendations = "Evacuate low lying areas immediately." if risk_level in ["High", "Critical"] else "No immediate action required."
        
        evidence = []
        if weather_data:
            evidence.append({"source": "Weather API", "description": weather_data.get('condition', 'Unknown weather condition')})
        if news_data:
            evidence.append({"source": "News Intel", "description": f"Found {len(news_data)} relevant alerts."})
        if docs:
            evidence.append({"source": "RAG System", "description": f"Consulted {len(docs)} historical SOPs."})
            
        report_data = {
            "summary": analysis,
            "confidence": confidence_score,
            "risk_level": risk_level,
            "evidence": evidence,
            "recommendation": recommendations
        }
        
        # 5. Executive Reporting (Generate Markdown)
        markdown_report = ExecutiveReporting.generate_report(report_data, format="markdown", language="English")

        # 6. Track LLMOps
        latency = time.time() - start_time
        tokens = len(markdown_report) // 4  # Rough heuristic
        cost = tokens * 0.000002
        LLMOpsTracker.track_execution(
            prompt=state.get("user_query", ""),
            response=markdown_report,
            tokens=tokens,
            cost=cost,
            latency=latency,
            agent="PolicyAgent"
        )

        return {
            'retrieved_documents': docs,
            'risk_level': risk_level,
            'confidence_score': confidence_score,
            'analysis': analysis,
            'recommendations': recommendations,
            'context': markdown_report,
            'execution_history': [f'PolicyAgent: Synthesized final report with Risk Level {risk_level} and Confidence {confidence_score}']
        }
