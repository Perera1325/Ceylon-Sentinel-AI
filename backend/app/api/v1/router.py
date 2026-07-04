from fastapi import APIRouter

from .endpoints import collectors, finance, health, news, stats, weather, ai

api_router = APIRouter()

api_router.include_router(news.router, prefix="/news", tags=["News"])
api_router.include_router(weather.router, prefix="/weather", tags=["Weather"])
api_router.include_router(finance.router, prefix="/finance", tags=["Finance"])
api_router.include_router(collectors.router, prefix="/collectors", tags=["Collectors"])
api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(stats.router, prefix="/stats", tags=["Statistics"])
api_router.include_router(ai.router, prefix="/ai", tags=["AI"])
