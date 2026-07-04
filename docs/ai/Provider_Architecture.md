# Provider Architecture

Details the BaseLLMProvider interface which all providers (OpenAI, Anthropic, Gemini, etc.) must implement. It guarantees standardized generate(), stream(), and health_check() methods.