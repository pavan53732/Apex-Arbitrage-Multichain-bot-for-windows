"""
Structured logging utilities.
"""

from __future__ import annotations
import logging
import sys
from typing import Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Create a structured logger for validators."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger


def get_validator_logger(validator_id: str) -> logging.Logger:
    """Get logger for a specific validator."""
    return setup_logger(f"validator.{validator_id}")