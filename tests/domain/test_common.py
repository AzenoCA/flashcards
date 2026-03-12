import pytest

from flashcards.domain.common import normalize_text


@pytest.mark.parametrize(
    ("raw_value", "expected"),
    [("abcde", "abcde"), ("   abcde", "abcde"), ("x" * 40, "x" * 40), ("  " + "x" * 40, "x" * 40)],
)
def test_normalize_text_returns_trimmed_value_with_allowed_length(raw_value: str, expected: str) -> None:
    assert normalize_text(raw_value, field_name="front") == expected


def test_normalize_text_rejects_empty_values_after_stripping() -> None:
    pass  # spacje, tabs i enter # with bd potrzebny context manager


def test_normalize_text_rejects_too_short_values() -> None:
    pass  # with bd potrzebny context manager


def test_normalize_text_rejects_too_long_values() -> None:
    pass  # with bd potrzebny context manager


def test_normalize_text_reports_the_provided_field_banes_in_error() -> None:
    pass  # with bd potrzebny context manager


# mozna uzyc parametrize tez
