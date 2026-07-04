from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import datetime
import asyncio
from sse_starlette.sse import EventSourceResponse
from ....ai.orchestrator.manager import WorkflowOrchestrator

router = APIRouter()
orchestrator = WorkflowOrchestrator()

class ChatRequest(BaseModel):
    user_query: str
    session_id: str

async def workflow_generator(request: ChatRequest):
    """
    Generator that simulates real-time streaming updates from the LangGraph workflow.
    In a true astream_events implementation, we would yield each node's completion.
    """
    initial_state = {
        "session_id": request.session_id,
        "request_id": f"req_{datetime.datetime.utcnow().timestamp()}",
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
    
    # Simulate Coordinator
    yield {"event": "progress", "data": '{"agent": "Coordinator", "status": "Started"}'}
    await asyncio.sleep(0.5)
    
    # Simulate Weather
    yield {"event": "progress", "data": '{"agent": "WeatherAgent", "status": "Analyzing"}'}
    await asyncio.sleep(0.5)
    
    # Simulate News
    yield {"event": "progress", "data": '{"agent": "NewsAgent", "status": "Analyzing"}'}
    await asyncio.sleep(0.5)
    
    # Simulate Policy
    yield {"event": "progress", "data": '{"agent": "PolicyAgent", "status": "Synthesizing"}'}
    
    # Actually run the workflow to get the final state
    result = await orchestrator.arun(initial_state)
    
    # Return the final result
    import json
    # Ensure dates are serialized
    safe_result = json.dumps({
        "status": "success",
        "answer": result.get("context", ""),
        "confidence": result.get("confidence_score", 0.0),
        "evidence": result.get("retrieved_documents", []),
        "risk_level": result.get("risk_level", "UNKNOWN")
    }, default=str)
    
    yield {"event": "complete", "data": safe_result}

@router.get("", summary="AI Chat Endpoint (SSE)")
async def chat_endpoint(user_query: str, session_id: str):
    request = ChatRequest(user_query=user_query, session_id=session_id)
    return EventSourceResponse(workflow_generator(request))
