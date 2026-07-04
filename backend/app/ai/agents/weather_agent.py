from .base import BaseAgent
from ..state.workflow_state import WorkflowState

class WeatherAgent(BaseAgent):
    def execute(self, state: WorkflowState) -> dict:
        return {'analysis': 'Weather conditions are stable.', 'execution_history': ['WeatherAgent executed']}
