from dataclasses import FrozenInstanceError
from datetime import UTC, datetime
from uuid import UUID

import pytest

from flashcards.domain.models import Flashcard, ReviewResult


@pytest.fixture
def card_id() -> UUID:
    """Return a stable UUID used by domain model."""
    return UUID("11111111-1111-1111-1111-111111111111")


@pytest.mark.parametrize(
    ("value", "expected"), [("again", ReviewResult.AGAIN), ("hard", ReviewResult.HARD), ("good", ReviewResult.GOOD)]
)
def test_review_result_parses_supported_wire_values(value: str, expected: ReviewResult) -> None:
    assert value == expected
    assert ReviewResult(value) is expected


def test_review_result_rejects_unknown_value() -> None:
    with pytest.raises(ValueError, match="'awesome' is not a valid ReviewResult"):
        ReviewResult("awesome")


def test_review_result_contract_stays_explicit() -> None:
    assert tuple(ReviewResult.__members__) == ("AGAIN", "HARD", "GOOD")
    assert tuple(result.value for result in ReviewResult) == ("again", "hard", "good")


def test_flashcard_uses_defaults_and_keeps_uuid_identifier(card_id: UUID) -> None:
    card = Flashcard(
        card_id=card_id,
        front="What is Python?",
        back="A programming language.",
        created_at=datetime.now(tz=UTC),
        updated_at=datetime.now(tz=UTC),
    )

    assert card.card_id is card_id
    assert card.review_count == 0
    assert card.interval_days == 0
    assert card.last_result is None


def test_flashcard_is_frozen(card_id: UUID) -> None:
    card = Flashcard(
        card_id=card_id,
        front="What is Python?",
        back="A programming language.",
        created_at=datetime.now(tz=UTC),
        updated_at=datetime.now(tz=UTC),
    )

    with pytest.raises(FrozenInstanceError):
        card.front = "Changed"


def test_flashcard_uses_slots(card_id: UUID) -> None:
    card = Flashcard(
        card_id=card_id,
        front="What is Python?",
        back="A programming language.",
        created_at=datetime.now(tz=UTC),
        updated_at=datetime.now(tz=UTC),
    )

    assert not hasattr(card, "__dict__")
