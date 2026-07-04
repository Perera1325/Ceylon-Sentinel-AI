from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ....database.connection import get_db
from ....schemas.collector_schema import (CollectorJobResponse,
                                          CollectorLogResponse)
from ....services.collector_service import collector_service

router = APIRouter()


@router.get(
    "", response_model=List[CollectorJobResponse], summary="Get all collector jobs"
)
async def get_collectors(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Retrieve all collector jobs."""
    return await collector_service.get_all_jobs(db, skip, limit)


@router.get(
    "/logs",
    response_model=List[CollectorLogResponse],
    summary="Get latest collector logs",
)
async def get_collector_logs(limit: int = 20, db: AsyncSession = Depends(get_db)):
    """Retrieve the most recent collector logs."""
    return await collector_service.get_latest_logs(db, limit)


@router.post("/run", summary="Trigger all collectors immediately")
async def trigger_all_collectors():
    """Manually trigger all registered collectors. Note: Actual triggering will be wired to the scheduler manager."""
    # Placeholder for Scheduler manager logic
    return {"message": "All collectors triggered"}


@router.post("/news", summary="Trigger News Collector")
async def trigger_news_collector():
    return {"message": "News collector triggered"}


@router.post("/weather", summary="Trigger Weather Collector")
async def trigger_weather_collector():
    return {"message": "Weather collector triggered"}


@router.post("/finance", summary="Trigger Finance Collector")
async def trigger_finance_collector():
    return {"message": "Finance collector triggered"}
