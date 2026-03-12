import pytest

from flashcards.domain.common import normalize_text
from flashcards.domain.errors import InvalidFlashcardError


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [("abcde", "abcde"), ("   abcde", "abcde"), ("x" * 40, "x" * 40), ("  " + ("x" * 40) + "   ", "x" * 40)],
)
def test_normalize_text_returns_trimmed_value_with_allowed_length(raw_value: str, expected: str) -> None:
    assert normalize_text(raw_value, field_name="front") == expected


@pytest.mark.parametrize("raw_value", ["", "   ", "\n\t  "])
def test_normalize_text_rejects_empty_values_after_stripping(raw_value: str) -> None:
    with pytest.raises(InvalidFlashcardError, match="front cannot be empty."):
        normalize_text(raw_value, field_name="front")


@pytest.mark.parametrize("raw_value", ["abcd", "  abcd  "])
def test_normalize_text_rejects_too_short_values(raw_value: str) -> None:
    with pytest.raises(InvalidFlashcardError, match="front must have between 5 and 40 characters."):
        normalize_text(raw_value, field_name="front")


def test_normalize_text_rejects_too_long_values() -> None:
    with pytest.raises(InvalidFlashcardError, match="front must have between 5 and 40 characters."):
        normalize_text("x" * 41, field_name="front")


def test_normalize_text_reports_the_provided_field_name_in_errors() -> None:
    with pytest.raises(InvalidFlashcardError, match="deck_name must have between 5 and 40 characters."):
        normalize_text("abcd", field_name="deck_name")
