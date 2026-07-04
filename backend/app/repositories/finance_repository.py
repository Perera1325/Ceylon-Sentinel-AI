from typing import List, Optional

from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.finance import Finance
from .base_repository import BaseRepository


class FinanceRepository(BaseRepository[Finance]):
    def __init__(self):
        super().__init__(Finance)

    async def get_latest(self, db: AsyncSession, limit: int = 10) -> List[Finance]:
        result = await db.execute(
            select(self.model).order_by(desc(self.model.timestamp)).limit(limit)
        )
        return list(result.scalars().all())


finance_repository = FinanceRepository()
