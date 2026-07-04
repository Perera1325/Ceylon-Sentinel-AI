# LLM Architecture

Outlines the overarching design of the AI Layer. The application requests generation via LLMService, which interfaces with a Provider Abstraction to call Concrete Providers. This decouples business logic from proprietary APIs.