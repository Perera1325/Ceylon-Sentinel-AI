from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.collectors import CollectorJobs, CollectorLogs
from ..repositories.collector_repository import (collector_job_repository,
                                                 collector_log_repository)


class CollectorService:
    async def get_all_jobs(
        self, db: AsyncSession, skip: int = 0, limit: int = 100
    ) -> List[CollectorJobs]:
        return await collector_job_repository.get_all(db, skip, limit)

    async def get_latest_logs(
        self, db: AsyncSession, limit: int = 20
    ) -> List[CollectorLogs]:
        return await collector_log_repository.get_latest_logs(db, limit)


collector_service = CollectorService()
