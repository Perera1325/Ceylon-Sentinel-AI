from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.news import News
from .base_repository import BaseRepository


class NewsRepository(BaseRepository[News]):
    def __init__(self):
        super().__init__(News)

    async def get_latest(self, db: AsyncSession, limit: int = 10) -> List[News]:
        result = await db.execute(
            select(self.model).order_by(desc(self.model.published_date)).limit(limit)
        )
        return list(result.scalars().all())

    async def get_by_category(
        self, db: AsyncSession, category: str, skip: int = 0, limit: int = 100
    ) -> List[News]:
        result = await db.execute(
            select(self.model)
            .filter(self.model.category == category)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    async def get_by_source(
        self, db: AsyncSession, source: str, skip: int = 0, limit: int = 100
    ) -> List[News]:
        result = await db.execute(
            select(self.model)
            .filter(self.model.source == source)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())


news_repository = NewsRepository()
