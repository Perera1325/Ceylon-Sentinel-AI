from typing import Dict, Type, Any

class AgentRegistry:
    """
    Registry for dynamic agent discovery and instantiation.
    """
    def __init__(self):
        self._agents: Dict[str, Any] = {}

    def register(self, name: str, agent_instance: Any) -> None:
        self._agents[name] = agent_instance

    def get_agent(self, name: str) -> Any:
        if name not in self._agents:
            raise ValueError(f"Agent {name} not found in registry")
        return self._agents[name]

    def list_agents(self) -> list:
        return list(self._agents.keys())
