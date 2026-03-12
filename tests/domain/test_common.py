import re

import pytest

from flashcards.domain.common import normalize_text
from flashcards.domain.errors import InvalidFlashcardError


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [
        ("abcde", "abcde"),
        ("   abcde", "abcde"),
        ("x" * 40, "x" * 40),
        (" " + ("x" * 40) + "  ", "x" * 40),
    ],
)
def test_normalize_text_return_trimmed_value_with_allowed_length(
    raw_value: str,
    expected: str,
) -> None:
    assert normalize_text(raw_value, field_name="front") == expected


@pytest.mark.parametrize(
    "raw_value",
    [
        "    ",
        "    " * 10,
    ],
)
def test_normalize_text_rejects_empty_values_after_stripping(raw_value: str) -> None:
    with pytest.raises(InvalidFlashcardError, match="front cannot be empty"):
        normalize_text(raw_value, field_name="front")


@pytest.mark.parametrize(
    "raw_value",
    [
        "abc",
        "abcd",
    ],
)
def test_normalize_text_rejects_too_short_values(raw_value: str) -> None:
    with pytest.raises(
        ValueError,
        match=re.escape("front must have between 5 and 40 characters."),
    ):
        normalize_text(raw_value, field_name="front")


@pytest.mark.parametrize(
    "raw_value",
    [
        "a" * 41,
        "a" * 100,
        " " + "a" * 41 + " ",
    ],
)
def test_normalize_text_rejects_too_long_values(raw_value: str) -> None:
    with pytest.raises(ValueError, match="between 5 and 40"):
        normalize_text(raw_value, field_name="front")


def test_normalize_text_reports_the_provided_field_name_in_errors() -> None:
    with pytest.raises(
        ValueError,
        match=re.escape("title must have between 5 and 40 characters."),
    ):
        normalize_text("11", field_name="title")
