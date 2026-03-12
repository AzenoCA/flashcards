import pytest

from flashcards.domain.common import normalize_text
from flashcards.domain.errors import InvalidFlashCardError


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [("abcde", "abcde"), ("   abcde", "abcde"), ("x" * 40, "x" * 40), ("  " + ("x" * 40) + "  ", "x" * 40)],
)
def test_normalize_text_returns_trimmed_value_with_allowed_length(raw_value: str, expected: str) -> None:
    assert normalize_text(raw_value, field_name="front") == expected


@pytest.mark.parametrize("raw_value", ["", "   ", "\n\t  "])
def test_normalize_text_rejects_empty_values_after_stripping(raw_value: str) -> None:
    with pytest.raises(InvalidFlashCardError, match="front cannot be empty."):
        normalize_text(raw_value, field_name="front")


@pytest.mark.parametrize("raw_value", ["abcd", " abcd "])
def test_normalize_text_reject_too_short_values(raw_value: str) -> None:
    with pytest.raises(InvalidFlashCardError, match="front must have between 5 and 40 characters."):
        normalize_text(raw_value, field_name="front")


@pytest.mark.parametrize("raw_value", ["x" * 50, "\t" + ("x" * 41) + "\n"])
def test_normalize_text_rejects_too_long_values(raw_value: str) -> None:
    with pytest.raises(InvalidFlashCardError, match="front must have between 5 and 40 characters."):
        normalize_text(raw_value, field_name="front")


@pytest.mark.parametrize(
    ("raw_value", "field_name", "error_message"),
    [("\n \n", "front", "front cannot be empty."), ("test", "back", "back must have between 5 and 40 characters.")],
)
def test_normalize_text_reports_the_provided_field_name_in_errors(
    raw_value: str, field_name: str, error_message: str
) -> None:
    with pytest.raises(InvalidFlashCardError, match=error_message):
        normalize_text(raw_value, field_name=field_name)
