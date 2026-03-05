from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import TYPE_CHECKING
from uuid import uuid4

from flashcards.services.utc_now import utc_now

if TYPE_CHECKING:
    from datetime import datetime
    from uuid import UUID


class ReviewResult(StrEnum):
    """Supported study outcomes for a review event."""

    AGAIN = "again"
    HARD = "hard"
    GOOD = "good"


@dataclass(frozen=True, slots=True)
class Flashcard:
    """Immutable flashcard entity."""

    front: str
    back: str
    card_id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)
    review_count: int = 0
    interval_days: int = 0
    last_result: ReviewResult | None = None
