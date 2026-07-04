from .base import BaseAgent
from ..state.workflow_state import WorkflowState

class CoordinatorAgent(BaseAgent):
    def execute(self, state: WorkflowState) -> dict:
        return {'execution_history': ['CoordinatorAgent executed']}
