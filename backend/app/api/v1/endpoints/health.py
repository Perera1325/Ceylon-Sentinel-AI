from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ....database.connection import get_db
from ....schemas.system_schema import SystemHealthResponse
from ....services.health_service import health_service

router = APIRouter()


@router.get(
    "", response_model=Dict[str, Any], summary="Get comprehensive health metrics"
)
async def get_health(db: AsyncSession = Depends(get_db)):
    """Retrieve the latest comprehensive health metrics for the entire system."""
    latest_health = await health_service.get_latest_health(db, limit=1)

    if latest_health:
        return {"status": "ok", "metrics": latest_health[0]}
    return {"status": "ok", "metrics": "No health data collected yet"}


@router.get("/status", summary="Alias for health")
async def get_status(db: AsyncSession = Depends(get_db)):
    """Alias for /health endpoint"""
    return await get_health(db)


@router.get("/ready", summary="Readiness probe")
async def readiness_probe(db: AsyncSession = Depends(get_db)):
    """K8s Readiness probe to check if the database is accessible."""
    try:
        from sqlalchemy import text

        await db.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception:
        from fastapi import HTTPException

        raise HTTPException(status_code=503, detail="Service Unavailable")


@router.get("/live", summary="Liveness probe")
async def liveness_probe():
    """K8s Liveness probe."""
    return {"status": "alive"}
