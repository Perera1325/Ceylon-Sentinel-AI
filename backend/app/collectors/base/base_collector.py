import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseCollector(ABC):
    """Abstract Base Class for all data collectors."""

    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"collector.{name}")
        self.is_healthy = True

    @abstractmethod
    async def initialize(self):
        """Initialize connections, setup clients, etc."""
        pass

    @abstractmethod
    async def collect(self) -> List[Dict[str, Any]]:
        """Collect data from the specific source(s)."""
        pass

    @abstractmethod
    def validate(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Validate raw collected data."""
        pass

    @abstractmethod
    def normalize(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize validated data into internal schema."""
        pass

    @abstractmethod
    async def save(self, data: List[Dict[str, Any]]):
        """Save normalized data to the database."""
        pass

    def health_check(self) -> bool:
        """Return the health status of the collector."""
        return self.is_healthy

    @abstractmethod
    async def shutdown(self):
        """Gracefully close connections and shutdown."""
        pass

    async def execute_pipeline(self):
        """Run the complete ingestion pipeline."""
        try:
            self.logger.info(f"Starting execution of {self.name}")
            raw_data = await self.collect()
            if not raw_data:
                self.logger.info("No data collected.")
                return

            validated_data = self.validate(raw_data)
            normalized_data = self.normalize(validated_data)

            await self.save(normalized_data)
            self.logger.info(f"Successfully processed {len(normalized_data)} records.")
            self.is_healthy = True

        except Exception as e:
            self.is_healthy = False
            self.logger.error(f"Error in {self.name} pipeline: {str(e)}", exc_info=True)
