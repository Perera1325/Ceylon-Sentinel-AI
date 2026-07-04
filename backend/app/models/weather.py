from sqlalchemy import Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import BaseModel


class Weather(BaseModel):
    __tablename__ = "weather"

    temperature: Mapped[float] = mapped_column(Float, nullable=False)
    humidity: Mapped[float] = mapped_column(Float, nullable=False)
    wind_speed: Mapped[float] = mapped_column(Float, nullable=False)
    pressure: Mapped[float] = mapped_column(Float, nullable=True)
    rainfall: Mapped[float] = mapped_column(Float, nullable=True)
    uv_index: Mapped[float] = mapped_column(Float, nullable=True)
    visibility: Mapped[float] = mapped_column(Float, nullable=True)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    district: Mapped[str] = mapped_column(String(100), nullable=True, index=True)
    province: Mapped[str] = mapped_column(String(100), nullable=True)
    forecast: Mapped[str] = mapped_column(Text, nullable=True)
    timestamp: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
