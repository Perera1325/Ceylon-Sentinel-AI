import logging
import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)


class TimingAndLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())

        # Add request_id to state
        request.state.request_id = request_id

        start_time = time.time()
        logger.info(f"[{request_id}] Started {request.method} {request.url.path}")

        response = await call_next(request)

        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        response.headers["X-Request-ID"] = request_id

        logger.info(
            f"[{request_id}] Completed {response.status_code} "
            f"in {process_time:.4f}s"
        )

        return response
