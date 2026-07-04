import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class WeatherBase(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    pressure: Optional[float] = None
    rainfall: Optional[float] = None
    uv_index: Optional[float] = None
    visibility: Optional[float] = None
    latitude: float
    longitude: float
    district: Optional[str] = None
    province: Optional[str] = None
    forecast: Optional[str] = None
    timestamp: str


class WeatherResponse(WeatherBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
