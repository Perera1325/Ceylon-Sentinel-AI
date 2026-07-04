from .base import BaseAgent
from ..state.workflow_state import WorkflowState
import json

class CoordinatorAgent(BaseAgent):
    async def execute(self, state: WorkflowState) -> dict:
        user_query = state.get("user_query", "")
        # Minimal coordination: just pass the query along and record execution
        return {
            'metadata': {'coordinator_decision': 'Invoke Weather, News, and Policy'},
            'execution_history': ['CoordinatorAgent: Received query and initiated workflow']
        }
