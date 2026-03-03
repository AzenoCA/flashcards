# pragma: no cover

import logging

from flashcards.utils.logging_config import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for the flashcards application."""
    configure_logging()
    logger.info("Application started")


if __name__ == "__main__":
    main()
