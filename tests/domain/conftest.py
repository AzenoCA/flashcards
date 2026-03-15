from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from flashcards.domain.models import Flashcards, RevievResult

if TYPE_CHECKING:
    import datetime


@pytest.fixture
def card_id() -> UUID:
    """Return a stable UUID used by domain model."""
    return UUID("11111111-1111-1111-1111-111111111111")


@pytest.fixture
def base_flashcard(card_id: UUID, fixed_now: datetime) -> Flashcards:
    """Provide a base Flashcards instance for tests.

    This fixture returns a flashcard with default values that can be reused
    across multiple tests. The card has no reviews yet and its timestamps
    are fixed to ensure deterministic test behavior.

    Args:
        card_id: Unique identifier for the flashcard provided by a fixture.
        fixed_now: Fixed datetime used for created and updated timestamps.

    Returns:
        Flashcards: A flashcard instance with predefined default values.
    """
    return Flashcards(
        card_id=card_id,
        front="What is python?",
        back="A programming language.",
        created_at=fixed_now,
        updated_at=fixed_now,
        review_count=0,
        interval_days=0,
        last_result=RevievResult.AGAIN,
    )
