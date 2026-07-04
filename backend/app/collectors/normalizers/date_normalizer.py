from datetime import datetime
from email.utils import parsedate_to_datetime

import dateutil.parser


class DateNormalizer:
    @staticmethod
    def normalize_date(date_string: str) -> str:
        """Convert various date formats into ISO 8601 UTC string."""
        if not date_string:
            return datetime.utcnow().isoformat()

        try:
            # Try parsing RSS date format (RFC 822)
            dt = parsedate_to_datetime(date_string)
            return dt.isoformat()
        except (TypeError, ValueError):
            pass

        try:
            # Fallback to dateutil parser
            dt = dateutil.parser.parse(date_string)
            return dt.isoformat()
        except Exception:
            # On failure, return current time
            return datetime.utcnow().isoformat()
