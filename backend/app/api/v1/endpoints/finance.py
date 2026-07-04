from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ....database.connection import get_db
from ....schemas.finance_schema import FinanceResponse
from ....services.finance_service import finance_service

router = APIRouter()


@router.get("", response_model=List[FinanceResponse], summary="Get all finance data")
async def get_finance(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Retrieve all financial records."""
    return await finance_service.get_latest_finance(db, limit)


@router.get(
    "/latest", response_model=List[FinanceResponse], summary="Get latest finance data"
)
async def get_latest_finance(limit: int = 10, db: AsyncSession = Depends(get_db)):
    """Retrieve the most recent financial records."""
    return await finance_service.get_latest_finance(db, limit)
