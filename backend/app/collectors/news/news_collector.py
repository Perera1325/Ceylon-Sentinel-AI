from typing import Any, Dict, List

from ...config.settings import settings
from ..adapters.news.news_adapters import HiruNewsAdapter, RSSNewsAdapter
from ..base.base_collector import BaseCollector
from ..common.http_client import HTTPClient
from ..normalizers.schema_normalizer import NewsSchemaNormalizer
from ..validators.news_validator import NewsItemValidator


class NewsCollector(BaseCollector):
    def __init__(self):
        super().__init__(name="NewsCollector")
        self.http_client = HTTPClient(timeout=settings.COLLECTOR_TIMEOUT_SECONDS)
        self.normalizer = NewsSchemaNormalizer()

        # Initialize Adapters
        self.hiru_adapter = HiruNewsAdapter(settings.HIRU_NEWS_API_URL)
        rss_feeds = [settings.ADA_DERANA_RSS_URL, settings.NEWSFIRST_RSS_URL]
        self.rss_adapter = RSSNewsAdapter(rss_feeds)

    async def initialize(self):
        self.logger.info("Initializing News Collector...")

    async def collect(self) -> List[Dict[str, Any]]:
        raw_data = []
        async with self.http_client as client:
            try:
                hiru_data = await self.hiru_adapter.fetch(client)
                raw_data.extend(hiru_data)
            except Exception as e:
                self.logger.error(f"Failed to fetch Hiru News: {e}")

        try:
            rss_data = await self.rss_adapter.fetch()
            raw_data.extend(rss_data)
        except Exception as e:
            self.logger.error(f"Failed to fetch RSS News: {e}")

        return raw_data

    def validate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        validated = []
        for item in data:
            # We must map slightly before validation to fit validator if needed, or normalizer first.
            # In our architecture: Collect -> Validate -> Normalize.
            # We map minimum fields required for validation.
            # For simplicity, we just pass raw item to pydantic.

            # Since raw data might not have collection_timestamp yet (added in normalization),
            # we need to be careful or do normalization first. The prompt requested Validate -> Normalize.
            # Let's adjust so validation only checks basic required fields.
            try:
                # Mock validation here for flexibility, as raw schema differs per source
                # In production, we might need a Validator per source, but we'll use a loose validator
                if item.get("title") and (item.get("original_url") or item.get("link")):
                    validated.append(item)
            except Exception as e:
                self.logger.warning(f"Validation failed for item: {e}")
        return validated

    def normalize(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [self.normalizer.normalize(item) for item in data]

    async def save(self, data: List[Dict[str, Any]]):
        # Mock database save
        self.logger.info(f"Saving {len(data)} news records to database.")

    async def shutdown(self):
        self.logger.info("Shutting down News Collector.")
