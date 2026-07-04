from typing import Any, Dict, List

from ...config.settings import settings
from ..adapters.weather.weather_adapters import OpenWeatherAdapter
from ..base.base_collector import BaseCollector
from ..common.http_client import HTTPClient
from ..normalizers.schema_normalizer import WeatherSchemaNormalizer
from ..validators.weather_validator import WeatherItemValidator


class WeatherCollector(BaseCollector):
    def __init__(self):
        super().__init__(name="WeatherCollector")
        self.http_client = HTTPClient(timeout=settings.COLLECTOR_TIMEOUT_SECONDS)
        self.normalizer = WeatherSchemaNormalizer()
        self.adapter = OpenWeatherAdapter(
            settings.OPENWEATHER_API_URL, settings.WEATHER_API_KEY
        )

    async def initialize(self):
        self.logger.info("Initializing Weather Collector...")

    async def collect(self) -> List[Dict[str, Any]]:
        async with self.http_client as client:
            try:
                return await self.adapter.fetch(client)
            except Exception as e:
                self.logger.error(f"Failed to fetch Weather: {e}")
                return []

    def validate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        validated = []
        for item in data:
            if item.get("temperature") is not None and item.get("latitude") is not None:
                validated.append(item)
        return validated

    def normalize(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [self.normalizer.normalize(item) for item in data]

    async def save(self, data: List[Dict[str, Any]]):
        self.logger.info(f"Saving {len(data)} weather records to database.")

    async def shutdown(self):
        self.logger.info("Shutting down Weather Collector.")
