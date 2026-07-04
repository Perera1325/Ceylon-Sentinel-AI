import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FinanceBase(BaseModel):
    currency: Optional[str] = None
    exchange_rate: Optional[float] = None
    gold_price: Optional[float] = None
    silver_price: Optional[float] = None
    fuel_price: Optional[float] = None
    timestamp: str


class FinanceResponse(FinanceBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
