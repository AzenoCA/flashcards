from datetime import UTC, datetime


def utc_now() -> datetime:
    """Return the current UTC datetime without microseconds.

    Returns:
        datetime: Current time in UTC with timezone information and
        microseconds set to 0.
    """
    return datetime.now(tz=UTC).replace(microsecond=0)
