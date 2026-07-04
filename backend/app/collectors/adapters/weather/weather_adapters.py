from typing import Any, Dict, List

from ...common.http_client import HTTPClient
from ...common.retry_handler import with_retry
from ...common.utils import parse_json_safe


class OpenWeatherAdapter:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key
        # Example Sri Lanka locations
        self.locations = ["Colombo", "Kandy", "Galle", "Jaffna"]

    @with_retry(max_retries=3)
    async def fetch(self, http_client: HTTPClient) -> List[Dict[str, Any]]:
        results = []
        for loc in self.locations:
            params = {"q": loc, "appid": self.api_key, "units": "metric"}
            response = await http_client.get(self.api_url, params=params)
            response.raise_for_status()
            data = parse_json_safe(response.text)

            # Map OpenWeather structure to flat dict for validation
            if data:
                mapped = {
                    "temperature": data.get("main", {}).get("temp"),
                    "feels_like": data.get("main", {}).get("feels_like"),
                    "humidity": data.get("main", {}).get("humidity"),
                    "pressure": data.get("main", {}).get("pressure"),
                    "wind_speed": data.get("wind", {}).get("speed"),
                    "wind_direction": data.get("wind", {}).get("deg"),
                    "latitude": data.get("coord", {}).get("lat"),
                    "longitude": data.get("coord", {}).get("lon"),
                    "district": loc,
                    "source": "OpenWeather",
                }
                results.append(mapped)

        return results
