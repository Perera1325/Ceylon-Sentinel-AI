from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database.base import BaseModel


class CollectorJobs(BaseModel):
    __tablename__ = "collector_jobs"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    interval_minutes: Mapped[int] = mapped_column(Integer, default=60)
    last_run: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    next_run: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)


class CollectorLogs(BaseModel):
    __tablename__ = "collector_logs"

    collector_name: Mapped[str] = mapped_column(String(100), index=True)
    provider: Mapped[str] = mapped_column(String(100), nullable=True)
    execution_time: Mapped[float] = mapped_column(Float, default=0.0)
    records_processed: Mapped[int] = mapped_column(Integer, default=0)
    records_saved: Mapped[int] = mapped_column(Integer, default=0)
    errors: Mapped[int] = mapped_column(Integer, default=0)
    warnings: Mapped[int] = mapped_column(Integer, default=0)
    retry_count: Mapped[int] = mapped_column(Integer, default=0)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class RSSSources(BaseModel):
    __tablename__ = "rss_sources"

    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(500), unique=True)
    category: Mapped[str] = mapped_column(String(100))
