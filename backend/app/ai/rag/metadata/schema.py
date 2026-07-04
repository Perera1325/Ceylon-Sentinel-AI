from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

class ChunkMetadata(BaseModel):
    document_id: str
    chunk_id: str
    title: Optional[str] = None
    source: str
    language: Optional[str] = "en"
    category: Optional[str] = None
    district: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = "Sri Lanka"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    hash: Optional[str] = None
    embedding_model: str
    version: str = "1.0"
    tags: List[str] = Field(default_factory=list)
