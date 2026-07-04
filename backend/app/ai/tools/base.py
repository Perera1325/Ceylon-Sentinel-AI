from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTool(ABC):
    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    async def execute(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def validate(self, input_data: Any) -> bool:
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass
