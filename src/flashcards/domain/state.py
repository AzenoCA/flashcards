from __future__ import annotations

from dataclasses import asdict

from flashcards.domain.common import normalize_text
from flashcards.domain.models import Flashcards, RevievResult
from flashcards.services.utc_now import utc_now


def add_flashcard(front: str, back: str) -> Flashcards:
    """Return a new flash card object."""
    normalized_front = normalize_text(front, field_name="front")
    normalized_back = normalize_text(back, field_name="back")

    return Flashcards(front=normalized_front, back=normalized_back)


def record_review(card: Flashcards, *, interval_days: int, last_result: RevievResult) -> Flashcards:
    """Create a new Flashcards instance with updated review information.

    Args:
        card: The flashcard that has been reviewed.
        interval_days: Number of days until the next review.
        last_result: Result of the last review attempt.

    Returns:
        Flashcards: A new Flashcards object with updated review metadata,
        including incremented review count, updated interval, last result,
        and updated timestamp.
    """
    data = asdict(card)
    data.update(
        {
            "updated_at": utc_now(),
            "review_count": card.review_count + 1,
            "interval_days": interval_days,
            "last_result": last_result,
        }
    )
    return Flashcards(**data)


def get_card_by_id(idx) -> Flashcards:  # noqa: ANN001
    """Retrieve a flashcard by its unique identifier.

    Args:
        idx: Identifier of the flashcard to retrieve.

    Returns:
        Flashcards: The flashcard with the given identifier.

    Raises:
        InvalidFlashcardError: If no flashcard with the given identifier exists.
    """
    ...
