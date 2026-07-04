import ssl
from typing import Any, Dict, Optional

import httpx


class HTTPClient:
    """Async HTTP Client for Collectors with connection pooling and timeouts."""

    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        # We can ignore SSL verification for certain feeds if needed, but safe default is True
        self.client = httpx.AsyncClient(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()

    async def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        if not self.client:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                return await client.get(url, headers=headers, params=params)
        return await self.client.get(url, headers=headers, params=params)

    async def post(
        self,
        url: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        if not self.client:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                return await client.post(url, json=json, headers=headers)
        return await self.client.post(url, json=json, headers=headers)
