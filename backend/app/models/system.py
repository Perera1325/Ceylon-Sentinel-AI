from datetime import datetime

from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import BaseModel


class SystemHealth(BaseModel):
    __tablename__ = "system_health"

    service_name: Mapped[str] = mapped_column(String(100), index=True)
    last_check: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow
    )
    cpu_usage: Mapped[float] = mapped_column(Float, nullable=True)
    memory_usage: Mapped[float] = mapped_column(Float, nullable=True)
    database_status: Mapped[str] = mapped_column(String(50), default="ok")
    redis_status: Mapped[str] = mapped_column(String(50), default="ok")
    qdrant_status: Mapped[str] = mapped_column(String(50), default="ok")


class ApiKeys(BaseModel):
    __tablename__ = "api_keys"

    name: Mapped[str] = mapped_column(String(100))
    key_hash: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
