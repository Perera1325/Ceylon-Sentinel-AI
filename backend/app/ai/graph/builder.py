from langgraph.graph import StateGraph, END
from ..state.workflow_state import WorkflowState
from ..agents.coordinator_agent import CoordinatorAgent
from ..agents.weather_agent import WeatherAgent
from ..agents.news_agent import NewsAgent
from ..agents.policy_agent import PolicyAgent

class GraphBuilder:
    def __init__(self):
        self.coordinator = CoordinatorAgent()
        self.weather = WeatherAgent()
        self.news = NewsAgent()
        self.policy = PolicyAgent()
        self.workflow = StateGraph(WorkflowState)

    def build(self):
        # Add Nodes
        self.workflow.add_node("coordinator", self.coordinator.execute)
        self.workflow.add_node("weather", self.weather.execute)
        self.workflow.add_node("news", self.news.execute)
        self.workflow.add_node("policy", self.policy.execute)

        # Add Edges
        self.workflow.set_entry_point("coordinator")
        self.workflow.add_edge("coordinator", "weather")
        self.workflow.add_edge("weather", "news")
        self.workflow.add_edge("news", "policy")
        self.workflow.add_edge("policy", END)

        return self.workflow.compile()
