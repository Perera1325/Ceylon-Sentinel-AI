from typing import Dict, Any

class ModelRegistry:
    """
    Registry for managing supported models and their metadata.
    """
    def __init__(self):
        self.models: Dict[str, Dict[str, Any]] = {
            "gpt-4o": {
                "provider": "openai",
                "context_window": 128000,
                "max_tokens": 4096,
                "pricing": {"input": 5.00, "output": 15.00}
            },
            "claude-3-5-sonnet": {
                "provider": "anthropic",
                "context_window": 200000,
                "max_tokens": 8192,
                "pricing": {"input": 3.00, "output": 15.00}
            },
            "default-model": {
                "provider": "default",
                "context_window": 8192,
                "max_tokens": 1024,
                "pricing": {"input": 0.0, "output": 0.0}
            }
        }

    def get_model_metadata(self, model_name: str) -> Dict[str, Any]:
        return self.models.get(model_name, self.models["default-model"])
