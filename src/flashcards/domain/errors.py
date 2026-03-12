class FlashCardsError(Exception):
    """Base exception for flashcards domain error."""


class InvalidFlashCardError(FlashCardsError):
    """Raised when a flashcard mutation request is invalid."""
