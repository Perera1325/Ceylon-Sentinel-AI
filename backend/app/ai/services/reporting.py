from typing import Dict, Any
import json
from datetime import datetime

class ExecutiveReporting:
    @staticmethod
    def generate_report(data: Dict[str, Any], format: str = "markdown", language: str = "English") -> str:
        """
        Generates an executive report in Markdown, JSON, or HTML.
        Handles formatting and multi-language structure.
        """
        summary = data.get("summary", "No summary provided.")
        confidence = data.get("confidence", 0.0)
        risk_level = data.get("risk_level", "Unknown")
        evidence = data.get("evidence", [])
        recommendation = data.get("recommendation", "")
        
        # In a real enterprise system, a translation model/API would be called here if language != "English"
        # For this sprint, we assume the LLM output (data) was already requested in the target language
        
        if format.lower() == "json":
            return json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "language": language,
                "executive_summary": summary,
                "risk_level": risk_level,
                "confidence": confidence,
                "evidence": evidence,
                "recommendations": recommendation
            }, indent=2)
            
        elif format.lower() == "html":
            ev_html = "".join([f"<li><strong>{e.get('source', '')}:</strong> {e.get('description', '')}</li>" for e in evidence])
            return f"""
            <div class="executive-report">
                <h2>Executive Summary</h2>
                <p><strong>Time:</strong> {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")} | <strong>Language:</strong> {language}</p>
                <p><strong>Risk Level:</strong> {risk_level} | <strong>Confidence:</strong> {confidence * 100}%</p>
                <p>{summary}</p>
                <h3>Supporting Evidence</h3>
                <ul>{ev_html}</ul>
                <h3>Recommendations</h3>
                <p>{recommendation}</p>
            </div>
            """
            
        else: # Markdown
            ev_md = "\n".join([f"- **{e.get('source', '')}**: {e.get('description', '')}" for e in evidence])
            return f"""# Executive Report ({language})
**Generated:** {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}
**Risk Level:** {risk_level} | **Confidence:** {confidence * 100}%

## Situation Overview
{summary}

## Supporting Evidence
{ev_md}

## Recommendations
{recommendation}
"""
