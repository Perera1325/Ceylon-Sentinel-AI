from typing import Dict, Any, List
from datetime import datetime
import uuid

class LLMOpsTracker:
    """
    In-memory tracker for LLMOps metrics to support Dashboard visualization.
    In production, this writes to PostgreSQL via SQLAlchemy.
    """
    _executions = []

    @classmethod
    def track_execution(cls, prompt: str, response: str, tokens: int, cost: float, latency: float, provider: str = "OpenAI", agent: str = "PolicyAgent", workflow: str = "DecisionWorkflow"):
        execution_record = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "prompt_length": len(prompt),
            "response_length": len(response),
            "tokens": tokens,
            "cost": cost,
            "latency": latency,
            "provider": provider,
            "agent": agent,
            "workflow": workflow,
            "status": "success" if latency < 15.0 else "warning" # Example metric
        }
        cls._executions.append(execution_record)
        return execution_record

    @classmethod
    def get_metrics(cls) -> Dict[str, Any]:
        total_tokens = sum(e["tokens"] for e in cls._executions)
        total_cost = sum(e["cost"] for e in cls._executions)
        avg_latency = sum(e["latency"] for e in cls._executions) / max(1, len(cls._executions))
        
        return {
            "total_executions": len(cls._executions),
            "total_tokens": total_tokens,
            "total_cost": round(total_cost, 4),
            "average_latency": round(avg_latency, 2),
            "recent_executions": cls._executions[-10:] # Return last 10
        }
