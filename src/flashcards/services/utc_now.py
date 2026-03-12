from datetime import UTC, datetime


def utc_now() -> datetime:
    """Returns utc now time."""
    return datetime.now(tz=UTC).replace(microsecond=0)
