from typing import Dict, Any
from pydantic import BaseModel

class SystemSettings(BaseModel):
    default_language: str = "English"
    risk_threshold_high: int = 60
    risk_threshold_critical: int = 85
    active_llm_provider: str = "OpenAI"
    fallback_llm_provider: str = "Anthropic"
    max_agent_retries: int = 3
    enable_auto_broadcast: bool = False

class SettingsManager:
    """
    Manages dynamic system settings for the application.
    In a production system, this data is cached in Redis and backed by PostgreSQL.
    """
    _current_settings = SystemSettings()

    @classmethod
    def get_settings(cls) -> SystemSettings:
        return cls._current_settings

    @classmethod
    def update_settings(cls, updates: Dict[str, Any]) -> SystemSettings:
        current_dict = cls._current_settings.model_dump()
        current_dict.update(updates)
        cls._current_settings = SystemSettings(**current_dict)
        # Here we would publish an invalidation event to Redis
        return cls._current_settings
