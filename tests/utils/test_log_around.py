from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from flashcards.utils.log_around import log_around

if TYPE_CHECKING:
    import pytest


def test_log_around_preserves_function_name() -> None:
    """Ensure the decorator preserves function metadata and return value."""

    @log_around
    def sample(value: int) -> int:
        """Increase value by 1."""
        return value + 1

    assert sample.__name__ == "sample"
    assert sample(1) == 2


def test_log_around_logs(caplog: pytest.LogCaptureFixture) -> None:
    """Ensure the decorator logs function call arguments and returned result."""

    @log_around
    def add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    with caplog.at_level(logging.DEBUG):
        add(2, 3)

    calling_record = caplog.records[0]
    returned_record = caplog.records[1]

    assert len(caplog.records) == 2
    assert calling_record.msg == "Calling %s"
    assert calling_record.args == (add.__qualname__,)
    assert calling_record.params == {"a": "2", "b": "3"}

    assert returned_record.msg == "Returned %s"
    assert returned_record.args == (add.__qualname__,)
    assert returned_record.output == "5"
