from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.system import SystemHealth
from .base_repository import BaseRepository


class HealthRepository(BaseRepository[SystemHealth]):
    def __init__(self):
        super().__init__(SystemHealth)

    async def get_latest_health(
        self, db: AsyncSession, limit: int = 10
    ) -> List[SystemHealth]:
        result = await db.execute(
            select(self.model).order_by(desc(self.model.last_check)).limit(limit)
        )
        return list(result.scalars().all())


health_repository = HealthRepository()
