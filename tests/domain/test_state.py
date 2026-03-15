from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import UUID

import pytest

import flashcards.domain.state as state_module
from flashcards.domain.errors import InvalidFlashcardError
from flashcards.domain.models import Flashcards, RevievResult
from flashcards.domain.state import add_flashcard, record_review

if TYPE_CHECKING:
    from uuid import UUID


def test_add_flashcard_returns_with_normalized_fields() -> None:
    card = add_flashcard("What is python?", "Programming language.")

    assert isinstance(card, Flashcards)
    assert card.front == "What is python?"
    assert card.back == "Programming language."


@pytest.mark.parametrize(
    ("front", "back"),
    [(" abc ", "valid back"), ("valid front", "x")],
)
def test_add_flashcard_validates_length(front: str, back: str) -> None:
    with pytest.raises(
        InvalidFlashcardError,
        match="must have between 5 and 40 characters.",
    ):
        add_flashcard(front=front, back=back)


def test_record_review_returns_updates_review_fields(
    base_flashcard: Flashcards, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(state_module, "utc_now", lambda: datetime(2026, 2, 10, 21, 37, 42, tzinfo=UTC))

    card = record_review(base_flashcard, interval_days=3, last_result=RevievResult.HARD)

    assert card.review_count == 1
    assert card.interval_days == 3
    assert card.last_result == RevievResult.HARD
    assert card.updated_at == datetime(2026, 2, 10, 21, 37, 42, tzinfo=UTC)


def test_record_review_preserves_unmodified_fields(
    base_flashcard: Flashcards, card_id: UUID, fixed_now: datetime
) -> None:
    card = record_review(base_flashcard, interval_days=3, last_result=RevievResult.HARD)

    assert card.front == "What is python?"
    assert card.back == "A programming language."
    assert card.card_id == card_id
    assert card.created_at == fixed_now
