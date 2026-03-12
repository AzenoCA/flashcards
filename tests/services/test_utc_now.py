# 1. czy dobry obiekt
# 2. czy dobra strefa
# 3. czy dobra data bo wywolujemy now()

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pytest

import flashcards.services.utc_now as utc_now_module
from flashcards.services.utc_now import utc_now


def test_utc_now_returns_utc_datetime_without_microseconds(
    fixed_now: datetime, frozen_datetime_class: object, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(utc_now_module, "datetime", frozen_datetime_class)

    value = utc_now()

    assert isinstance(value, datetime)
    assert value.tzinfo is UTC
    assert value.microsecond == 0
    assert value == fixed_now
