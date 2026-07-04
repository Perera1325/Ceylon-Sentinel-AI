from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class BaseValidator(BaseModel):
    """Base Pydantic model for validating collected items."""

    source: str = Field(..., description="Source of the data")
    collection_timestamp: str = Field(
        ..., description="ISO 8601 UTC timestamp of collection"
    )
    unique_hash: str = Field(..., description="SHA-256 hash for deduplication")

    @classmethod
    def validate_item(cls, item: Dict[str, Any]) -> Optional["BaseValidator"]:
        try:
            return cls(**item)
        except Exception as e:
            # Here we might log the validation error using a common logger
            import logging

            logging.getLogger(__name__).warning(f"Validation failed for item: {e}")
            return None
