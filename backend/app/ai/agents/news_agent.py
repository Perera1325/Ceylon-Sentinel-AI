from .base import BaseAgent
from ..state.workflow_state import WorkflowState
from ..tools.news_tool import NewsTool

class NewsAgent(BaseAgent):
    def __init__(self):
        self.news_tool = NewsTool()
        self.news_tool.initialize()

    async def execute(self, state: WorkflowState) -> dict:
        news_data = await self.news_tool.execute(query=state.get("user_query", ""))
        
        return {
            'news_data': news_data,
            'execution_history': ['NewsAgent: Collected relevant news']
        }
