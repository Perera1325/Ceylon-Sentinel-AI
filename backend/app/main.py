import logging
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from sqlalchemy.exc import SQLAlchemyError

from app.api.v1.router import api_router
from app.config.settings import settings
from app.core.exceptions import (
    not_found_exception_handler,
    validation_exception_handler,
    sqlalchemy_exception_handler,
    global_exception_handler
)
from app.core.middleware import TimingAndLoggingMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from app.scheduler.manager import shutdown_scheduler, start_scheduler
from pythonjsonlogger import jsonlogger

# Configure structured logging
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
    rename_fields={"levelname": "level", "asctime": "timestamp"}
)
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
# Remove default handlers to avoid duplicates
for handler in logger.handlers[:-1]:
    logger.removeHandler(handler)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Ceylon Sentinel AI Backend...")
    start_scheduler()
    yield
    # Shutdown
    logger.info("Shutting down Ceylon Sentinel AI Backend...")
    shutdown_scheduler()


app = FastAPI(
    title="Ceylon Sentinel AI",
    description="Enterprise-grade AI Platform for Disaster Prediction & Public Safety in Sri Lanka.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response

app.add_middleware(SecurityHeadersMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3002", "http://localhost:8000", "https://admin.ceylonsentinel.ai", "https://app.ceylonsentinel.ai"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
# Configure allowed hosts if strictly required
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"]) # Configured via Ingress in k8s
app.add_middleware(TimingAndLoggingMiddleware)

# Exception Handlers
app.add_exception_handler(404, not_found_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

# Include Routers
app.include_router(api_router, prefix=settings.API_V1_STR)

# Instrument metrics
Instrumentator().instrument(app).expose(app, endpoint="/api/v1/metrics")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Ceylon Sentinel AI API",
        "docs": "/docs",
        "health": "/api/v1/health",
    }
