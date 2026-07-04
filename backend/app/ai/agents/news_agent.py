from .base import BaseAgent
from ..state.workflow_state import WorkflowState

class NewsAgent(BaseAgent):
    def execute(self, state: WorkflowState) -> dict:
        return {'context': 'Extracted news entities.', 'execution_history': ['NewsAgent executed']}
