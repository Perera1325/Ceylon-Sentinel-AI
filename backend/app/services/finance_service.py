from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.finance import Finance
from ..repositories.finance_repository import finance_repository


class FinanceService:
    async def get_latest_finance(
        self, db: AsyncSession, limit: int = 10
    ) -> List[Finance]:
        return await finance_repository.get_latest(db, limit)


finance_service = FinanceService()
