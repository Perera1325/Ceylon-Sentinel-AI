from typing import List, Dict, Any
from datetime import datetime

class TimelineGenerator:
    @staticmethod
    def extract_timeline(events_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extracts temporal events and constructs an incident timeline.
        """
        timeline = []
        for event in events_data:
            if "time" in event and "description" in event:
                timeline.append({
                    "timestamp": event["time"],
                    "event": event["description"],
                    "source": event.get("source", "System")
                })
        
        # If no explicit events provided, generate a synthetic one for the execution
        if not timeline:
            timeline.append({
                "timestamp": datetime.utcnow().strftime("%H:%M:%S"),
                "event": "AI Analysis Initiated",
                "source": "Coordinator Agent"
            })
            timeline.append({
                "timestamp": datetime.utcnow().strftime("%H:%M:%S"),
                "event": "Weather & News Scanned",
                "source": "Sub-agents"
            })
            
        return sorted(timeline, key=lambda x: x["timestamp"])
