from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    query: str
    session_id: str
    trace_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class AgentResponse(BaseModel):
    agent_name: str
    status: str
    confidence: float
    summary: str
    recommendation: Optional[str] = None
    execution_time: float
    metadata: Dict[str, Any] = Field(default_factory=dict)
