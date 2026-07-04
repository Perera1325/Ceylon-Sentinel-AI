from typing import Dict, Any, List

class RiskEngine:
    @staticmethod
    def calculate_risk(weather_data: Dict[str, Any], news_data: List[Dict[str, Any]], rag_docs: List[Any]) -> Dict[str, Any]:
        """
        Calculate risk score 0-100 based on anomalies and severity.
        """
        score = 0.0
        
        # Weather severity (0-50 points)
        if weather_data:
            anomaly_score = weather_data.get("anomaly_score", 0.0)
            score += min(50.0, anomaly_score * 50.0)
            
        # News severity (0-30 points)
        if news_data:
            high_risk_keywords = ["flood", "landslide", "cyclone", "warning", "critical", "evacuate"]
            news_score = 0
            for item in news_data:
                text = str(item).lower()
                for kw in high_risk_keywords:
                    if kw in text:
                        news_score += 5
            score += min(30.0, float(news_score))
            
        # RAG context matches (0-20 points)
        if rag_docs:
            score += min(20.0, len(rag_docs) * 5.0)
            
        # Cap at 100
        final_score = min(100.0, score)
        
        # Determine Level
        if final_score < 30:
            level = "Low"
        elif final_score < 60:
            level = "Medium"
        elif final_score < 85:
            level = "High"
        else:
            level = "Critical"
            
        return {
            "score": round(final_score, 1),
            "level": level
        }
