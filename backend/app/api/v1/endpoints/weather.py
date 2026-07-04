from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ....database.connection import get_db
from ....schemas.weather_schema import WeatherResponse
from ....services.weather_service import weather_service

router = APIRouter()


@router.get("", response_model=List[WeatherResponse], summary="Get all weather data")
async def get_weather(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Retrieve all weather records."""
    return await weather_service.get_latest_weather(db, limit)


@router.get(
    "/latest", response_model=List[WeatherResponse], summary="Get latest weather"
)
async def get_latest_weather(limit: int = 10, db: AsyncSession = Depends(get_db)):
    """Retrieve the most recent weather records."""
    return await weather_service.get_latest_weather(db, limit)


@router.get(
    "/district/{district}",
    response_model=List[WeatherResponse],
    summary="Get weather by district",
)
async def get_weather_by_district(
    district: str, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Retrieve weather records filtered by district."""
    return await weather_service.get_weather_by_district(db, district, skip, limit)
