import asyncio
import logging
from typing import List

from ..base.base_collector import BaseCollector


class CollectorManager:
    """Manages registration, scheduling, and execution of collectors."""

    def __init__(self):
        self.collectors: List[BaseCollector] = []
        self.logger = logging.getLogger(__name__)

    def register(self, collector: BaseCollector):
        """Register a new collector."""
        self.collectors.append(collector)
        self.logger.info(f"Registered collector: {collector.name}")

    async def initialize_all(self):
        """Initialize all registered collectors."""
        for collector in self.collectors:
            try:
                await collector.initialize()
            except Exception as e:
                self.logger.error(f"Failed to initialize {collector.name}: {e}")

    async def run_once(self):
        """Run all collectors once concurrently."""
        tasks = [collector.execute_pipeline() for collector in self.collectors]
        await asyncio.gather(*tasks, return_exceptions=True)
        self._log_health()

    async def start_scheduling(self, interval_seconds: int = 300):
        """Run collectors on a schedule."""
        self.logger.info(f"Starting scheduler with interval {interval_seconds}s")
        await self.initialize_all()
        try:
            while True:
                await self.run_once()
                await asyncio.sleep(interval_seconds)
        except asyncio.CancelledError:
            self.logger.info("Scheduler cancelled. Shutting down...")
        finally:
            await self.shutdown_all()

    def _log_health(self):
        """Log health status of all collectors."""
        for collector in self.collectors:
            status = "HEALTHY" if collector.health_check() else "UNHEALTHY"
            self.logger.info(f"Collector {collector.name} status: {status}")

    async def shutdown_all(self):
        """Gracefully shutdown all collectors."""
        for collector in self.collectors:
            try:
                await collector.shutdown()
            except Exception as e:
                self.logger.error(f"Error shutting down {collector.name}: {e}")
