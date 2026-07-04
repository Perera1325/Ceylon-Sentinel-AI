from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.collectors import CollectorJobs, CollectorLogs
from .base_repository import BaseRepository


class CollectorJobRepository(BaseRepository[CollectorJobs]):
    def __init__(self):
        super().__init__(CollectorJobs)

    async def get_by_name(self, db: AsyncSession, name: str) -> Optional[CollectorJobs]:
        result = await db.execute(select(self.model).filter(self.model.name == name))
        return result.scalars().first()


class CollectorLogRepository(BaseRepository[CollectorLogs]):
    def __init__(self):
        super().__init__(CollectorLogs)

    async def get_latest_logs(
        self, db: AsyncSession, limit: int = 20
    ) -> List[CollectorLogs]:
        result = await db.execute(
            select(self.model).order_by(desc(self.model.started_at)).limit(limit)
        )
        return list(result.scalars().all())


collector_job_repository = CollectorJobRepository()
collector_log_repository = CollectorLogRepository()
