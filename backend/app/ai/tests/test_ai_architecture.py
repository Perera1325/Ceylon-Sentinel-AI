import pytest
from ...ai.schemas.request import LLMRequest
from ...ai.services.llm_service import LLMService

@pytest.mark.asyncio
async def test_llm_service_initialization():
    service = LLMService()
    assert "openai" in service.providers
    assert "anthropic" in service.providers

def test_llm_request_validation():
    # Test valid request
    req = LLMRequest(user_prompt="Hello")
    assert req.user_prompt == "Hello"
    assert req.max_tokens == 1024
    assert req.temperature == 0.7

@pytest.mark.asyncio
async def test_placeholder_provider_generation():
    service = LLMService()
    req = LLMRequest(user_prompt="Test")
    res = await service.generate_response(req, "openai")
    
    assert res.provider == "openai"
    assert "Placeholder response" in res.answer
