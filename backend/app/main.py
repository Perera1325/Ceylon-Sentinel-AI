from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Ceylon Sentinel AI",
    description="Backend API for Ceylon Sentinel AI Platform",
    version="0.1.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Ceylon Sentinel AI Backend...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Ceylon Sentinel AI Backend...")

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "service": "Ceylon Sentinel AI API"}

# Include routers here in the future
# app.include_router(some_router)
