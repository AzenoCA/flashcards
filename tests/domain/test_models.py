from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import UTC, datetime
from typing import TYPE_CHECKING

import pytest

from flashcards.domain import Flashcards, RevievResult

if TYPE_CHECKING:
    from uuid import UUID


@pytest.mark.parametrize(
    ("value", "expected"), [("again", RevievResult.AGAIN), ("hard", RevievResult.HARD), ("good", RevievResult.GOOD)]
)
def test_review_result_parses_supported_values(value: str, expected: RevievResult) -> None:
    assert value == expected
    assert RevievResult(value) is expected


def test_review_result_reject_unknow_value() -> None:
    with pytest.raises(ValueError, match="'awesome' is not a valid RevievResult"):
        RevievResult("awesome")


def test_review_result_contract_stays_explicite() -> None:
    assert tuple(RevievResult.__members__) == ("AGAIN", "HARD", "GOOD")
    assert tuple(result.value for result in RevievResult) == ("again", "hard", "good")


def test_flashcards_uses_defaults_and_keeps_uuid_identifier(card_id: UUID) -> None:

    card = Flashcards(
        card_id=card_id,
        front="What is python",
        back="A programming language",
        created_at=datetime.now(tz=UTC),
        updated_at=datetime.now(tz=UTC),
    )

    assert card.card_id is card_id
    assert card.review_count == 0
    assert card.interval_days == 0
    assert card.last_result is None


def test_flashcard_is_frozen(card_id: UUID) -> None:
    card = Flashcards(
        card_id=card_id,
        front="What is python",
        back="A programming language",
        created_at=datetime.now(tz=UTC),
        updated_at=datetime.now(tz=UTC),
    )

    with pytest.raises(FrozenInstanceError):
        card.front = "Chahnged"


def test_flashcard_uses_slots(card_id: UUID) -> None:
    card = Flashcards(
        card_id=card_id,
        front="What is python",
        back="A programming language",
        created_at=datetime.now(tz=UTC),
        updated_at=datetime.now(tz=UTC),
    )

    assert not hasattr(card, "__dict__")
