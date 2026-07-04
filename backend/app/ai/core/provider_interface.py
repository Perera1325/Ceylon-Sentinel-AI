from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Dict, List

from ..schemas.request import LLMRequest
from ..schemas.response import LLMResponse


class BaseLLMProvider(ABC):
    """
    Abstract Base Class representing an LLM Provider interface.
    Every concrete provider must implement these methods to be injected into the LLM service.
    """

    @abstractmethod
    def initialize(self) -> None:
        """Initialize any required clients or configurations."""
        pass

    @abstractmethod
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate a complete text response given an LLMRequest."""
        pass

    @abstractmethod
    async def stream(self, request: LLMRequest) -> AsyncGenerator[str, None]:
        """Stream the generated response back as partial chunks."""
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Ping the provider to check API availability."""
        pass

    @abstractmethod
    async def list_models(self) -> List[str]:
        """List available models for this provider."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Cleanup resources on shutdown."""
        pass

    @abstractmethod
    def estimate_tokens(self, text: str) -> int:
        """Estimate the number of tokens in the given text."""
        pass

    @abstractmethod
    def estimate_cost(self, request: LLMRequest, response: LLMResponse = None) -> float:
        """Estimate the cost of the request/response in USD."""
        pass

    @abstractmethod
    def validate_request(self, request: LLMRequest) -> bool:
        """Validate if the request conforms to the provider's capabilities."""
        pass

    @abstractmethod
    def validate_response(self, response: Any) -> bool:
        """Validate the provider's raw response format."""
        pass
