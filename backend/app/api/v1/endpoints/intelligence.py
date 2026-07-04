from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any, List
from pydantic import BaseModel

from app.ai.services.risk_engine import RiskEngine
from app.ai.services.confidence_engine import ConfidenceEngine
from app.ai.services.reporting import ExecutiveReporting
from app.ai.services.timeline import TimelineGenerator
from app.ai.evaluation.evaluator import EvaluationFramework, HallucinationDetector
from app.ai.telemetry.llmops import LLMOpsTracker

router = APIRouter()

class ReportRequest(BaseModel):
    summary: str
    evidence: List[Dict[str, str]]
    confidence: float
    risk_level: str
    recommendation: str
    language: str = "English"
    format: str = "markdown"

class RiskRequest(BaseModel):
    weather_data: Dict[str, Any]
    news_data: List[Dict[str, Any]]
    rag_docs: List[Any]

class EvalRequest(BaseModel):
    response_text: str
    context_docs: List[str]

@router.get("/risk")
async def get_risk(weather_anomaly: float = 0.0, news_count: int = 0, rag_count: int = 0):
    """Calculate current system risk level."""
    # For GET, we simulate based on query params. Real implementation would use POST with full body.
    weather_data = {"anomaly_score": weather_anomaly} if weather_anomaly > 0 else {}
    news_data = [{"description": "flood warning"} for _ in range(news_count)]
    rag_docs = ["doc" for _ in range(rag_count)]
    
    return RiskEngine.calculate_risk(weather_data, news_data, rag_docs)

@router.get("/confidence")
async def get_confidence(weather_success: bool = True, news_success: bool = True, rag_count: int = 5):
    """Calculate system confidence."""
    score = ConfidenceEngine.calculate_confidence(weather_success, news_success, rag_count)
    return {"confidence_score": score}

@router.get("/timeline")
async def get_timeline():
    """Get recent incident timeline."""
    return TimelineGenerator.extract_timeline([]) # Will generate synthetic recent timeline

@router.get("/llmops")
async def get_llmops_metrics():
    """Get LLMOps telemetry and costs."""
    return LLMOpsTracker.get_metrics()

@router.post("/evaluation")
async def evaluate_response(req: EvalRequest):
    """Evaluate an LLM response for groundedness and hallucinations."""
    eval_results = EvaluationFramework.evaluate_response(req.response_text, req.context_docs)
    hallucination_check = HallucinationDetector.detect(req.response_text, req.context_docs)
    
    return {
        "evaluation": eval_results,
        "hallucination": hallucination_check
    }

@router.post("/report")
async def generate_report(req: ReportRequest):
    """Generate an executive report in multiple languages/formats."""
    report_content = ExecutiveReporting.generate_report(req.model_dump(), req.format, req.language)
    return {"report": report_content, "format": req.format, "language": req.language}
