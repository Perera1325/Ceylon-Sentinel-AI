from ..graph.builder import GraphBuilder
from ..state.workflow_state import WorkflowState
from typing import Dict, Any

class WorkflowOrchestrator:
    def __init__(self):
        self.graph = GraphBuilder().build()

    async def arun(self, initial_state: Dict[str, Any]) -> dict:
        """Executes the LangGraph workflow with the given initial state."""
        return await self.graph.ainvoke(initial_state)
