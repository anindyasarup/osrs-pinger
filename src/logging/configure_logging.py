"""
Configure logging for the project.

This module initializes the Python 'logging' module with a predefined 
configuration enabling consistent logging settings throughout the project.
The logging level format, and handlers are set to ensure standardized log 
messages are generated accross different modules.

Usage:
    To use logging in your project, simply import this module and call the 
    'config_logging.py' function with the log_level parameter before any 
    logging statements. The logging configuration will then be applied to 
    all loggers used within the project.
"""
import logging


def config_logging(log_level: int):
    """
    Configure Python 'logging' module with the given 'log_level'

    Args:
        log_level (int): log_level to configure the logging at program entry.
    """
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
