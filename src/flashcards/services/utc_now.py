from datetime import UTC, datetime


def utc_now() -> datetime:
    """Returned date."""
    return datetime.now(tz=UTC).replace(microsecond=0)
