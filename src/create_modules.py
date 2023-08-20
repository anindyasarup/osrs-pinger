"""
This module provides a function for setting up essential modules required 
for the project's execution. It follows the principles of dependency 
injection to setup singleton instances of modules used in the project.
"""
from logger.setup_logger import LoggerSingleton


def create_modules(config: dict) -> dict:
    """
    Creates a modules dictionary maps to initialized modules to emulate 
    dependency injection principles based on the provided configuration.

    Args:
        config (dict): A dictionary containing configuration details, including logger settings.

    Returns:
        dict: Returns a dictionary containing inialized modules
    """
    modules = {}

    logger = LoggerSingleton(log_folder=config['logger']['log_folder'],
                             log_filename=config['logger']['log_filename'])

    modules['logger'] = logger

    return modules
