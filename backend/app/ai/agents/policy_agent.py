from .base import BaseAgent
from ..state.workflow_state import WorkflowState

class PolicyAgent(BaseAgent):
    def execute(self, state: WorkflowState) -> dict:
        return {'recommendations': 'Evacuate low lying areas.', 'execution_history': ['PolicyAgent executed']}
