from flashcards.domain.errors import InvalidFlashCardError


def normalize_text(value: str, *, field_name: str) -> str:
    """Strip and validate required text fileds."""
    normalized = value.strip()

    if not normalized:
        raise InvalidFlashCardError(f"{field_name} cannot be empty.")

    if not 5 <= len(normalized) <= 40:
        raise InvalidFlashCardError(f"{field_name} must have between 5 and 40 characters.")

    return normalized
