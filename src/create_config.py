"""
This module provides a function for generating a configuration dictionary based on 
the data stored in a JSON configuration file.
"""
from pathlib import Path
import json


def create_config() -> dict:
    """
    Reads the contents of 'config.json', processes the data, and maps it to the
    configuration dictionary with relevant information.

    Returns:
        dict: config mapped to config.json
    """
    with open('src/config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    config = {}

    logger = {}
    logger["log_folder"] = Path(config_data['logger']['folder_location'])
    logger["log_filename"] = config_data['logger']['file_name']

    config["logger"] = logger

    return config
