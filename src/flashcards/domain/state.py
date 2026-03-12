from __future__ import annotations

from flashcards.domain.common import normalize_text
from flashcards.domain.models import Flashcards


def add_flashcard(front: str, back: str) -> Flashcards:
    """Return a new flash card object."""
    normalized_front = normalize_text(front, field_name="front")
    normalized_front = normalize_text(back, field_name="back")

    return Flashcards(front=normalized_front, back=normalized_front)
