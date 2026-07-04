from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class LLMResponse(BaseModel):
    answer: str = Field(..., description="The generated text from the model")
    provider: str = Field(..., description="The provider used (e.g., openai, anthropic)")
    model: str = Field(..., description="The specific model used (e.g., gpt-4o)")
    latency: float = Field(..., description="Time taken to generate response in seconds")
    prompt_tokens: Optional[int] = Field(default=None, description="Tokens used for the prompt")
    completion_tokens: Optional[int] = Field(default=None, description="Tokens used for the completion")
    total_tokens: Optional[int] = Field(default=None, description="Total tokens used")
    estimated_cost: Optional[float] = Field(default=None, description="Estimated cost in USD")
    finish_reason: Optional[str] = Field(default="stop", description="Reason the model stopped generating")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Time the response was generated")
