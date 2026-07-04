import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ....database.connection import get_db
from ....schemas.news_schema import NewsResponse
from ....services.news_service import news_service

router = APIRouter()


@router.get("", response_model=List[NewsResponse], summary="Get all news")
async def get_news(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """Retrieve all news articles with pagination."""
    # Temporarily using get_latest as a placeholder for get_all with pagination
    # In a real app we would have a specific get_all method
    return await news_service.get_latest_news(db, limit)


@router.get("/latest", response_model=List[NewsResponse], summary="Get latest news")
async def get_latest_news(limit: int = 10, db: AsyncSession = Depends(get_db)):
    """Retrieve the most recent news articles."""
    return await news_service.get_latest_news(db, limit)


@router.get(
    "/category/{category}",
    response_model=List[NewsResponse],
    summary="Get news by category",
)
async def get_news_by_category(
    category: str, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Retrieve news articles filtered by category."""
    return await news_service.get_news_by_category(db, category, skip, limit)


@router.get(
    "/source/{source}", response_model=List[NewsResponse], summary="Get news by source"
)
async def get_news_by_source(
    source: str, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Retrieve news articles filtered by source."""
    return await news_service.get_news_by_source(db, source, skip, limit)


@router.get("/{id}", response_model=NewsResponse, summary="Get news by ID")
async def get_news_by_id(id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    """Retrieve a specific news article by its UUID."""
    news_item = await news_service.get_news_by_id(db, id)
    if not news_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="News not found"
        )
    return news_item
