from fastapi import APIRouter, Depends
from typing import List, Dict, Any
from ....ai.schemas.request import LLMRequest
from ....ai.schemas.response import LLMResponse
from ....ai.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.get("/providers", summary="List all supported LLM providers")
async def get_providers():
    return {"providers": list(llm_service.providers.keys())}

@router.get("/models", summary="List models for a specific provider")
async def get_models(provider: str = "openai"):
    p = llm_service.get_provider(provider)
    models = await p.list_models()
    return {"provider": provider, "models": models}

@router.get("/health", summary="Check health of all AI providers")
async def get_ai_health():
    health = {}
    for name, provider in llm_service.providers.items():
        health[name] = await provider.health_check()
    return health

@router.post("/chat", response_model=LLMResponse, summary="Send a request to the LLM")
async def chat_with_llm(request: LLMRequest, provider: str = "openai"):
    return await llm_service.generate_response(request, provider_name=provider)

@router.post("/estimate", summary="Estimate cost and tokens for a request")
async def estimate_request(request: LLMRequest):
    return {"estimated_tokens": len(request.user_prompt.split()), "estimated_cost_usd": 0.0}
