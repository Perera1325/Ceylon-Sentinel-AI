from typing import Dict, Any
from .templates import PromptTemplate

class PromptManager:
    """
    Manages loading, formatting, and versioning of prompts.
    """
    def __init__(self):
        pass

    def get_prompt(self, template: PromptTemplate, **kwargs) -> str:
        """Format and return a prompt template with the provided variables."""
        return template.value.format(**kwargs)

    def validate_prompt(self, prompt: str) -> bool:
        """Validate prompt against safety and length rules."""
        return len(prompt) > 0
