from typing import Dict, Any, List

class ConfidenceEngine:
    @staticmethod
    def calculate_confidence(weather_success: bool, news_success: bool, rag_count: int, llm_certainty: float = 0.9) -> float:
        """
        Calculate an overall confidence score based on input sources and agent reliability.
        """
        score = 0.0
        
        # Tool success weight (0.4)
        tool_score = 0.0
        if weather_success: tool_score += 0.2
        if news_success: tool_score += 0.2
        score += tool_score
        
        # RAG Context weight (0.3)
        rag_score = min(0.3, rag_count * 0.1)
        score += rag_score
        
        # LLM Certainty weight (0.3)
        score += (llm_certainty * 0.3)
        
        return round(min(1.0, score), 2)
