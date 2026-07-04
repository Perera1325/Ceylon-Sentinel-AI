import asyncio
import time


class RateLimiter:
    """Simple Async Token Bucket Rate Limiter for Collectors."""

    def __init__(self, calls: int, period: float):
        self.calls = calls
        self.period = period
        self.tokens = calls
        self.last_updated = time.monotonic()
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_updated
            self.tokens = min(
                self.calls, self.tokens + elapsed * (self.calls / self.period)
            )
            self.last_updated = now

            if self.tokens < 1:
                sleep_time = (1 - self.tokens) / (self.calls / self.period)
                await asyncio.sleep(sleep_time)
                self.tokens = 0
                self.last_updated = time.monotonic()
            else:
                self.tokens -= 1
