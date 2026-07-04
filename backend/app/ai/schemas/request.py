from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class LLMRequest(BaseModel):
    system_prompt: Optional[str] = Field(default=None, description="System level instructions for the model")
    user_prompt: str = Field(..., description="The main input prompt from the user")
    conversation_history: List[Dict[str, str]] = Field(default_factory=list, description="Previous messages in format [{'role': 'user', 'content': '...'}, ...]")
    temperature: float = Field(default=0.7, description="Sampling temperature (0.0 to 1.0)")
    max_tokens: int = Field(default=1024, description="Maximum tokens to generate")
    stream: bool = Field(default=False, description="Whether to stream the response")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional context or provider specific args")
    user_id: Optional[str] = Field(default=None, description="Identifier for the user making the request")
    session_id: Optional[str] = Field(default=None, description="Identifier for the conversation session")
    trace_id: Optional[str] = Field(default=None, description="Tracing ID for observability")
