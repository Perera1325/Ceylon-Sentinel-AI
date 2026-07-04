from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseNormalizer(ABC):
    """Abstract base class for all normalizers."""

    @abstractmethod
    def normalize(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize raw data into internal unified schema."""
        pass
