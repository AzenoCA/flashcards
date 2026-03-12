class FlashcardsError(Exception):
    """Base exception for flashcards domain errors."""


class InvalidFlashcardError(FlashcardsError):
    """Raised when a flashcard mutation request is invalid."""
