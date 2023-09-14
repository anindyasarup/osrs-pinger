"""
This module provides a function for setting up essential modules required 
for the project's execution. It follows the principles of dependency 
injection to setup singleton instances of modules used in the project.
"""
from logger.create_logger import LoggerSingleton
import process
import pinger


def create_modules(config: dict) -> dict:
    """
    Creates a modules dictionary maps to initialized modules to emulate 
    dependency injection principles based on the provided configuration.

    Args:
        config (dict): A dictionary containing configuration details, including logger settings.

    Returns:
        dict: Returns a dictionary containing inialized modules
    """

    logger = LoggerSingleton(log_folder=config['logger']['log_folder'],
                             log_filename=config['logger']['log_filename'])

    modules = {}
    modules['logger'] = logger
    modules['process'] = process
    modules['pinger'] = pinger

    return modules
