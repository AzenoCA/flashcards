from datetime import UTC, datetime


def utc_now() -> datetime:
    """Return the current UTC time with microseconds set to zero.

    Returns:
        datetime: Current time in the UTC timezone with microseconds truncated.
    """
    return datetime.now(tz=UTC).replace(microsecond=0)
