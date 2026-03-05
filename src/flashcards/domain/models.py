from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING

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
    """Immutable flascard entity."""

    card_id: UUID
    front: str
    back: str
    create_at: datetime
    update_at: datetime
    review_count: int = 0
    interval_days: int = 0
    last_result: ReviewResult | None = None
