import logging
import logging.config
import os

from pythonjsonlogger import json


def configure_logging() -> None:
    """Configure loggers, handlers, and formatters."""
    level: str = os.getenv("LOG_LEVEL", "INFO").upper()

    handlers = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": level,
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json",
            "level": level,
            "filename": "app.log",
            "maxBytes": 10_485_760,
            "backupCount": 5,
            "encoding": "utf-8",
        },
    }

    formatters = {
        "json": {"()": json.JsonFormatter, "format": "%(asctime)s %(name)s %(levelname)s %(message)s %(module)s"}
    }

    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": formatters,
            "handlers": handlers,
            "root": {"handlers": ["console", "file"], "level": level},
        }
    )
