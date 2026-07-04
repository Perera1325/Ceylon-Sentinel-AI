from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.weather import Weather
from .base_repository import BaseRepository


class WeatherRepository(BaseRepository[Weather]):
    def __init__(self):
        super().__init__(Weather)

    async def get_latest(self, db: AsyncSession, limit: int = 10) -> List[Weather]:
        result = await db.execute(
            select(self.model).order_by(desc(self.model.timestamp)).limit(limit)
        )
        return list(result.scalars().all())

    async def get_by_district(
        self, db: AsyncSession, district: str, skip: int = 0, limit: int = 100
    ) -> List[Weather]:
        result = await db.execute(
            select(self.model)
            .filter(self.model.district == district)
            .order_by(desc(self.model.timestamp))
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())


weather_repository = WeatherRepository()
