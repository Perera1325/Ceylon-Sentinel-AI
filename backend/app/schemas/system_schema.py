import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SystemHealthResponse(BaseModel):
    id: uuid.UUID
    service_name: str
    last_check: datetime
    cpu_usage: Optional[float]
    memory_usage: Optional[float]
    database_status: str
    redis_status: str
    qdrant_status: str

    model_config = ConfigDict(from_attributes=True)
