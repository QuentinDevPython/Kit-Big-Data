"""This module implements the app loggers."""

import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

# Debug
debug_handler = logging.FileHandler(
    Path(__file__).parent / "logs" / "debug.log"
)
debug_handler.setLevel(logging.DEBUG)

debug_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
debug_handler.setFormatter(debug_formatter)

logger = logging.getLogger()
logger.addHandler(debug_handler)

# Erreurs
error_handler = logging.FileHandler(
    Path(__file__).parent / "logs" / "error.log"
)
error_handler.setLevel(logging.ERROR)

error_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
error_handler.setFormatter(error_formatter)

logger = logging.getLogger()
logger.addHandler(error_handler)
