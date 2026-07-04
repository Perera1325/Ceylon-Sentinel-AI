import json
from typing import Any, Dict

from ..common.utils import current_timestamp, generate_hash
from .base_normalizer import BaseNormalizer
from .date_normalizer import DateNormalizer


class NewsSchemaNormalizer(BaseNormalizer):
    def normalize(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize raw news data into Ceylon Sentinel internal schema."""
        normalized = {
            "title": raw_data.get("title", "").strip(),
            "summary": raw_data.get("summary", ""),
            "description": raw_data.get("description", ""),
            "content": raw_data.get("content", ""),
            "image_url": raw_data.get("image_url", ""),
            "published_date": DateNormalizer.normalize_date(
                raw_data.get("published_date", "")
            ),
            "author": raw_data.get("author", "Unknown"),
            "category": raw_data.get("category", "General"),
            "original_url": raw_data.get("original_url", ""),
            "language": raw_data.get("language", "en"),
            "district": raw_data.get("district", None),
            "country": raw_data.get("country", "Sri Lanka"),
            "source": raw_data.get("source", "Unknown"),
            "collection_timestamp": current_timestamp(),
        }

        # Create a unique hash based on URL and Title to avoid duplicates
        hash_input = f"{normalized['original_url']}_{normalized['title']}"
        normalized["unique_hash"] = generate_hash(hash_input)

        return normalized


class WeatherSchemaNormalizer(BaseNormalizer):
    def normalize(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize raw weather data into internal schema."""
        normalized = {
            "temperature": float(raw_data.get("temperature", 0.0)),
            "feels_like": raw_data.get("feels_like"),
            "humidity": float(raw_data.get("humidity", 0.0)),
            "pressure": raw_data.get("pressure"),
            "wind_speed": float(raw_data.get("wind_speed", 0.0)),
            "wind_direction": raw_data.get("wind_direction"),
            "rainfall": raw_data.get("rainfall"),
            "cloud_coverage": raw_data.get("cloud_coverage"),
            "visibility": raw_data.get("visibility"),
            "uv_index": raw_data.get("uv_index"),
            "latitude": float(raw_data.get("latitude", 0.0)),
            "longitude": float(raw_data.get("longitude", 0.0)),
            "district": raw_data.get("district"),
            "province": raw_data.get("province"),
            "forecast": raw_data.get("forecast"),
            "timestamp": DateNormalizer.normalize_date(raw_data.get("timestamp", "")),
            "source": raw_data.get("source", "Unknown"),
            "collection_timestamp": current_timestamp(),
        }

        hash_input = f"{normalized['source']}_{normalized['latitude']}_{normalized['longitude']}_{normalized['timestamp']}"
        normalized["unique_hash"] = generate_hash(hash_input)

        return normalized


class FinanceSchemaNormalizer(BaseNormalizer):
    def normalize(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        normalized = {
            "usd_lkr": float(raw_data.get("usd_lkr", 0.0)),
            "eur_lkr": raw_data.get("eur_lkr"),
            "gbp_lkr": raw_data.get("gbp_lkr"),
            "jpy_lkr": raw_data.get("jpy_lkr"),
            "inr_lkr": raw_data.get("inr_lkr"),
            "gold_price": raw_data.get("gold_price"),
            "silver_price": raw_data.get("silver_price"),
            "diesel_price": raw_data.get("diesel_price"),
            "petrol_price": raw_data.get("petrol_price"),
            "exchange_timestamp": DateNormalizer.normalize_date(
                raw_data.get("exchange_timestamp", "")
            ),
            "source": raw_data.get("source", "Unknown"),
            "collection_timestamp": current_timestamp(),
        }

        hash_input = f"{normalized['source']}_{normalized['exchange_timestamp']}"
        normalized["unique_hash"] = generate_hash(hash_input)

        return normalized
