from ..schemas.request import LLMRequest
from ..schemas.response import LLMResponse
from ..models.registry import ModelRegistry

class CostEstimator:
    """
    Service to estimate and track token costs.
    """
    def __init__(self):
        self.registry = ModelRegistry()

    def estimate_cost(self, model: str, prompt_tokens: int, completion_tokens: int = 0) -> float:
        metadata = self.registry.get_model_metadata(model)
        pricing = metadata.get("pricing", {"input": 0.0, "output": 0.0})
        # Assuming pricing is per 1M tokens as standard
        input_cost = (prompt_tokens / 1_000_000) * pricing["input"]
        output_cost = (completion_tokens / 1_000_000) * pricing["output"]
        return input_cost + output_cost
