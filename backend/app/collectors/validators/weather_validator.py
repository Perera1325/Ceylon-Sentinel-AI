from typing import Optional

from pydantic import Field

from .base_validator import BaseValidator


class WeatherItemValidator(BaseValidator):
    temperature: float
    feels_like: Optional[float] = None
    humidity: float
    pressure: Optional[float] = None
    wind_speed: float
    wind_direction: Optional[float] = None
    rainfall: Optional[float] = None
    cloud_coverage: Optional[float] = None
    visibility: Optional[float] = None
    uv_index: Optional[float] = None
    latitude: float
    longitude: float
    district: Optional[str] = None
    province: Optional[str] = None
    forecast: Optional[str] = None
    timestamp: str
