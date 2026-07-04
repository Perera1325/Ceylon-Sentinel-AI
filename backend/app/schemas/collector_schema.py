import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CollectorJobResponse(BaseModel):
    id: uuid.UUID
    name: str
    interval_minutes: int
    last_run: Optional[datetime]
    next_run: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


class CollectorLogResponse(BaseModel):
    id: uuid.UUID
    collector_name: str
    provider: Optional[str]
    execution_time: float
    records_processed: int
    records_saved: int
    errors: int
    warnings: int
    retry_count: int
    started_at: datetime
    finished_at: datetime

    model_config = ConfigDict(from_attributes=True)
