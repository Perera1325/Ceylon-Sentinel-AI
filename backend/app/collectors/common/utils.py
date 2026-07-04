import hashlib
import json
from datetime import datetime
from typing import Any, Dict


def generate_hash(content: str) -> str:
    """Generate a SHA-256 hash for unique identification of records."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def parse_json_safe(response_text: str) -> Dict[str, Any]:
    """Safely parse JSON and return empty dict on failure."""
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {}


def current_timestamp() -> str:
    """Return ISO format current UTC timestamp."""
    return datetime.utcnow().isoformat()
