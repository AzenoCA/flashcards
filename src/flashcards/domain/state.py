from __future__ import annotations

from flashcards.domain.common import normalize_text
from flashcards.domain.models import Flashcard


def add_flashcard(
    front: str,
    back: str,
) -> Flashcard:
    """Return new flashcard object."""
    normalized_front: str = normalize_text(front, field_name="front")
    normalized_back: str = normalize_text(back, field_name="back")

    return Flashcard(front=normalized_front, back=normalized_back)
