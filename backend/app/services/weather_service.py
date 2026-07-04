from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.weather import Weather
from ..repositories.weather_repository import weather_repository


class WeatherService:
    async def get_latest_weather(
        self, db: AsyncSession, limit: int = 10
    ) -> List[Weather]:
        return await weather_repository.get_latest(db, limit)

    async def get_weather_by_district(
        self, db: AsyncSession, district: str, skip: int = 0, limit: int = 100
    ) -> List[Weather]:
        return await weather_repository.get_by_district(db, district, skip, limit)


weather_service = WeatherService()
