from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import flashcards.services.utc_now as utc_now_module
from flashcards.services.utc_now import utc_now

if TYPE_CHECKING:
    import pytest


def test_utc_now_returns_utc_datetime_without_microseconds(
    fixed_now: datetime, frozen_datetime_class: object, monkeypatch: pytest.MonkeyPatch
) -> None:

    monkeypatch.setattr(utc_now_module, "datetime", frozen_datetime_class)

    value = utc_now()

    assert isinstance(value, datetime)
    assert value.microsecond == 0
    assert value == fixed_now
