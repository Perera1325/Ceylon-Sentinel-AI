from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
import operator
from typing import Annotated

class WorkflowState(TypedDict):
    """
    Shared state for the LangGraph multi-agent workflow.
    """
    session_id: str
    request_id: str
    user_query: str
    
    # Context injected by agents
    weather_data: Optional[Dict[str, Any]]
    news_data: Optional[List[Dict[str, Any]]]
    retrieved_documents: Optional[List[Dict[str, Any]]]
    
    # Processed Analysis
    context: str
    analysis: str
    recommendations: str
    confidence_score: float
    risk_level: str
    
    # Orchestration metadata
    execution_history: Annotated[List[str], operator.add]
    errors: Annotated[List[str], operator.add]
    metadata: Dict[str, Any]
    timestamp: datetime
