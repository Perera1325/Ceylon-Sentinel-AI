from abc import ABC, abstractmethod
from typing import Any
from ..state.workflow_state import WorkflowState

class BaseAgent(ABC):
    @abstractmethod
    def execute(self, state: WorkflowState) -> dict:
        pass
