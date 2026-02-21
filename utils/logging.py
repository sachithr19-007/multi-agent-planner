"""
Logging configuration for the Multi-Agent Task Planning System.

Provides consistent, production-ready logging setup across all modules.
"""

import logging
import sys
from typing import Optional

from multi_agent_planner.config import get_settings


def setup_logging(
    level: Optional[str] = None,
    format_string: Optional[str] = None,
) -> None:
    """
    Configure application-wide logging.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR). Uses config if not set.
        format_string: Custom format string. Uses config if not set.
    """
    settings = get_settings()
    log_level = level or settings.log_level
    log_format = format_string or settings.log_format

    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for the given module name.

    Args:
        name: Module name, typically __name__.

    Returns:
        Configured Logger instance.
    """
    return logging.getLogger(name)
