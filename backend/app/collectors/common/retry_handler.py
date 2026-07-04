import logging

import httpx
from tenacity import (retry, retry_if_exception_type, stop_after_attempt,
                      wait_exponential)

logger = logging.getLogger(__name__)


def log_retry_attempt(retry_state):
    """Log when a retry happens."""
    logger.warning(
        f"Retrying: {retry_state.fn.__name__} attempt {retry_state.attempt_number}"
    )


def with_retry(max_retries: int = 3):
    """
    Decorator for retrying async functions on network errors.
    Uses exponential backoff.
    """
    return retry(
        stop=stop_after_attempt(max_retries),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((httpx.RequestError, httpx.TimeoutException)),
        after=log_retry_attempt,
        reraise=True,
    )
