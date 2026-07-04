from typing import Any, Dict, List

from ...common.http_client import HTTPClient
from ...common.retry_handler import with_retry
from ...common.utils import parse_json_safe


class ExchangeRateAdapter:
    def __init__(self, api_url: str):
        self.api_url = api_url

    @with_retry(max_retries=3)
    async def fetch(self, http_client: HTTPClient) -> List[Dict[str, Any]]:
        response = await http_client.get(self.api_url)
        response.raise_for_status()
        data = parse_json_safe(response.text)

        rates = data.get("rates", {})
        if not rates:
            return []

        mapped = {
            "usd_lkr": rates.get("LKR", 0.0),  # Assuming base is USD
            "source": "ExchangeRate-API",
            "exchange_timestamp": data.get("time_last_update_utc"),
        }
        return [mapped]
