from typing import Dict, Optional, Any
from ..core.provider_interface import BaseLLMProvider
from ..schemas.request import LLMRequest
from ..schemas.response import LLMResponse
from ..providers.openai_provider import OpenAIProvider
from ..providers.anthropic_provider import AnthropicProvider

class LLMService:
    """
    Primary orchestration service for routing LLM requests to the appropriate provider.
    """
    def __init__(self):
        self.providers: Dict[str, BaseLLMProvider] = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider(),
        }

    def get_provider(self, provider_name: str) -> BaseLLMProvider:
        provider = self.providers.get(provider_name.lower())
        if not provider:
            # Fallback provider logic could go here
            provider = self.providers["openai"]
        return provider

    async def generate_response(self, request: LLMRequest, provider_name: str = "openai") -> LLMResponse:
        provider = self.get_provider(provider_name)
        if not provider.validate_request(request):
            raise ValueError("Invalid request for provider")
        
        response = await provider.generate(request)
        
        if not provider.validate_response(response):
            raise ValueError("Provider returned an invalid response")
            
        return response
