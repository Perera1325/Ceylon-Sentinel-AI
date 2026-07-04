from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.system import SystemHealth
from ..repositories.health_repository import health_repository


class HealthService:
    async def get_latest_health(
        self, db: AsyncSession, limit: int = 1
    ) -> List[SystemHealth]:
        return await health_repository.get_latest_health(db, limit)


health_service = HealthService()
