from fastapi import APIRouter

router = APIRouter()


@router.get("", summary="Get global statistics")
async def get_stats():
    """Retrieve high-level ingestion statistics and records counts."""
    # Placeholder for actual stats gathering logic
    return {
        "total_news_records": 0,
        "total_weather_records": 0,
        "total_finance_records": 0,
        "active_collectors": 3,
    }
