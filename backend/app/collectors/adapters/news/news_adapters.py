from typing import Any, Dict, List

from ...common.http_client import HTTPClient
from ...common.retry_handler import with_retry
from ...common.utils import parse_json_safe
from ...rss.rss_client import RSSClient


class HiruNewsAdapter:
    def __init__(self, api_url: str):
        self.api_url = api_url

    @with_retry(max_retries=3)
    async def fetch(self, http_client: HTTPClient) -> List[Dict[str, Any]]:
        response = await http_client.get(self.api_url)
        response.raise_for_status()
        data = parse_json_safe(response.text)
        # Assuming the API returns a list of news in 'articles' key
        return data.get("articles", [])


class RSSNewsAdapter:
    def __init__(self, feed_urls: List[str]):
        self.rss_client = RSSClient(feed_urls=feed_urls)

    async def fetch(self) -> List[Dict[str, Any]]:
        return await self.rss_client.fetch_feeds()
