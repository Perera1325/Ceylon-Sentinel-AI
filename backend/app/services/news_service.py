from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.news import News
from ..repositories.news_repository import news_repository


class NewsService:
    async def get_latest_news(self, db: AsyncSession, limit: int = 10) -> List[News]:
        return await news_repository.get_latest(db, limit)

    async def get_news_by_category(
        self, db: AsyncSession, category: str, skip: int = 0, limit: int = 100
    ) -> List[News]:
        return await news_repository.get_by_category(db, category, skip, limit)

    async def get_news_by_source(
        self, db: AsyncSession, source: str, skip: int = 0, limit: int = 100
    ) -> List[News]:
        return await news_repository.get_by_source(db, source, skip, limit)

    async def get_news_by_id(self, db: AsyncSession, news_id: str) -> News:
        return await news_repository.get_by_id(db, news_id)


news_service = NewsService()
