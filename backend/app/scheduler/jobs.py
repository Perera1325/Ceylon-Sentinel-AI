import logging

from ..collectors.finance.finance_collector import FinanceCollector
from ..collectors.news.news_collector import NewsCollector
from ..collectors.weather.weather_collector import WeatherCollector
from ..database.session import async_session_factory

logger = logging.getLogger(__name__)


async def run_news_collector():
    logger.info("Starting scheduled job: News Collector")
    collector = NewsCollector()
    await collector.initialize()
    await collector.execute_pipeline()
    await collector.shutdown()


async def run_weather_collector():
    logger.info("Starting scheduled job: Weather Collector")
    collector = WeatherCollector()
    await collector.initialize()
    await collector.execute_pipeline()
    await collector.shutdown()


async def run_finance_collector():
    logger.info("Starting scheduled job: Finance Collector")
    collector = FinanceCollector()
    await collector.initialize()
    await collector.execute_pipeline()
    await collector.shutdown()
