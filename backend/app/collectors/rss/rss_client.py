import logging
from typing import Any, Dict, List

import feedparser

logger = logging.getLogger(__name__)


class RSSClient:
    """Reusable RSS framework for parsing feeds."""

    def __init__(self, feed_urls: List[str]):
        self.feed_urls = feed_urls

    async def fetch_feeds(self) -> List[Dict[str, Any]]:
        """Fetch and parse all registered RSS feeds synchronously via feedparser but wrapped in async."""
        import asyncio

        loop = asyncio.get_running_loop()

        all_entries = []
        for url in self.feed_urls:
            try:
                # feedparser.parse blocks, so run in executor
                parsed_feed = await loop.run_in_executor(None, feedparser.parse, url)

                if parsed_feed.bozo:
                    logger.warning(
                        f"Malformed XML in feed: {url} - {parsed_feed.bozo_exception}"
                    )

                for entry in parsed_feed.entries:
                    entry_dict = {
                        "title": getattr(entry, "title", ""),
                        "summary": getattr(entry, "summary", ""),
                        "description": getattr(
                            entry, "description", getattr(entry, "summary", "")
                        ),
                        "content": getattr(entry, "content", ""),
                        "original_url": getattr(entry, "link", url),
                        "published_date": getattr(entry, "published", ""),
                        "author": getattr(entry, "author", "Unknown"),
                        "source": url,
                    }
                    # Extract image if present
                    if hasattr(entry, "media_content") and entry.media_content:
                        entry_dict["image_url"] = entry.media_content[0].get("url", "")

                    all_entries.append(entry_dict)

            except Exception as e:
                logger.error(f"Error parsing feed {url}: {e}")

        return all_entries
