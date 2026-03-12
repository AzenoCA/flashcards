from __future__ import annotations

from flashcards.domain.common import normalize_text
from flashcards.domain.models import Flashcard


def add_flashcards(
    front: str,
    back: str,
) -> Flashcard:
    """Return new flashcard object."""
    normalized_front = normalize_text(front, field_name="front")
    normalized_back = normalize_text(back, field_name="front")

    return Flashcard(front=normalized_front, back=normalized_back)
