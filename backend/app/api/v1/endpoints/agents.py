from fastapi import APIRouter
from typing import Dict, Any, List
from pydantic import BaseModel
import datetime
from ....ai.orchestrator.manager import WorkflowOrchestrator

router = APIRouter()
orchestrator = WorkflowOrchestrator()

class AgentRunRequest(BaseModel):
    session_id: str
    request_id: str
    user_query: str

@router.post("/run", summary="Execute the multi-agent workflow")
async def run_agents(request: AgentRunRequest):
    initial_state = {
        "session_id": request.session_id,
        "request_id": request.request_id,
        "user_query": request.user_query,
        "weather_data": None,
        "news_data": None,
        "retrieved_documents": None,
        "context": "",
        "analysis": "",
        "recommendations": "",
        "confidence_score": 0.0,
        "risk_level": "UNKNOWN",
        "execution_history": [],
        "errors": [],
        "metadata": {},
        "timestamp": datetime.datetime.utcnow()
    }
    result = orchestrator.run(initial_state)
    return {"status": "success", "result": result}

@router.get("", summary="List registered agents")
async def list_agents():
    return {"agents": ["coordinator", "weather", "news", "policy"]}

@router.get("/graph", summary="Get graph structure")
async def get_graph():
    return {"nodes": ["coordinator", "weather", "news", "policy"]}

@router.get("/workflows", summary="List available workflows")
async def list_workflows():
    return {"workflows": ["default_disaster_response"]}

@router.get("/status", summary="Check agent health status")
async def get_status():
    return {"status": "healthy"}
