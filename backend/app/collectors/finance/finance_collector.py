from typing import Any, Dict, List

from ...config.settings import settings
from ..adapters.finance.finance_adapters import ExchangeRateAdapter
from ..base.base_collector import BaseCollector
from ..common.http_client import HTTPClient
from ..normalizers.schema_normalizer import FinanceSchemaNormalizer
from ..validators.finance_validator import FinanceItemValidator


class FinanceCollector(BaseCollector):
    def __init__(self):
        super().__init__(name="FinanceCollector")
        self.http_client = HTTPClient(timeout=settings.COLLECTOR_TIMEOUT_SECONDS)
        self.normalizer = FinanceSchemaNormalizer()
        self.adapter = ExchangeRateAdapter(settings.EXCHANGE_RATE_API_URL)

    async def initialize(self):
        self.logger.info("Initializing Finance Collector...")

    async def collect(self) -> List[Dict[str, Any]]:
        async with self.http_client as client:
            try:
                return await self.adapter.fetch(client)
            except Exception as e:
                self.logger.error(f"Failed to fetch Finance data: {e}")
                return []

    def validate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        validated = []
        for item in data:
            if item.get("usd_lkr") is not None:
                validated.append(item)
        return validated

    def normalize(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [self.normalizer.normalize(item) for item in data]

    async def save(self, data: List[Dict[str, Any]]):
        self.logger.info(f"Saving {len(data)} finance records to database.")

    async def shutdown(self):
        self.logger.info("Shutting down Finance Collector.")
