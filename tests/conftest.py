from datetime import UTC, datetime, timezone

import pytest


@pytest.fixture(scope="session")
def fixed_now() -> datetime:
    """Return a stable timestamp used for time-freezing tests."""
    return datetime(2026, 2, 10, 21, 37, 42, tzinfo=UTC)


@pytest.fixture(scope="session")
def frozen_datetime_class(fixed_now: datetime) -> object:
    """Return a datetime replacement exposing a deterministic ``now``."""

    class _FrozenDateTime:
        @staticmethod
        def now(tz: timezone) -> datetime:
            assert tz is UTC
            return fixed_now

    return _FrozenDateTime
