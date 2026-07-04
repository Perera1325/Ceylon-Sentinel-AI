from pydantic import BaseModel, Field
from typing import List, Optional

class Evidence(BaseModel):
    source: str = Field(description="The source of the evidence (e.g., Weather API, News API, RAG Document)")
    description: str = Field(description="A brief description of what the evidence proves")

class ExplainableReport(BaseModel):
    summary: str = Field(description="A comprehensive executive summary of the decision")
    evidence: List[Evidence] = Field(description="List of supporting evidence used to make the decision")
    confidence: float = Field(description="A confidence score between 0.0 and 1.0", ge=0.0, le=1.0)
    limitations: List[str] = Field(description="Any limitations or missing context in this decision")
    recommendation: str = Field(description="The final actionable recommendation")
    language: str = Field(description="The language of this report (e.g., English, Sinhala, Tamil)", default="English")

class HallucinationCheck(BaseModel):
    is_supported: bool = Field(description="True if the statement is fully supported by evidence")
    unsupported_claims: List[str] = Field(description="List of any claims that are not supported by the provided context")
