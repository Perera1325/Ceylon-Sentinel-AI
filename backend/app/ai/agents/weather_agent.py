from .base import BaseAgent
from ..state.workflow_state import WorkflowState
from ..tools.weather_tool import WeatherTool
import asyncio

class WeatherAgent(BaseAgent):
    def __init__(self):
        self.weather_tool = WeatherTool()
        self.weather_tool.initialize()

    async def execute(self, state: WorkflowState) -> dict:
        weather_data = await self.weather_tool.execute()
        
        return {
            'weather_data': weather_data,
            'execution_history': ['WeatherAgent: Collected real-time weather']
        }
