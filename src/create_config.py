"""
This module provides a function for generating a configuration dictionary based on 
the data stored in a JSON configuration file.

Functions:
    create_config()
        Reads the contents of 'src/config.json', processes the data, and creates a
        configuration dictionary with relevant information.

Usage:
    To use this module, import it and call the 'create_config()' function. This function reads the
    JSON configuration file and extracts information such as log file details.
"""
from pathlib import Path
import os
import json


def create_config():
    with open('src/config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    config = {}

    logger = {}
    logger["log_folder"] = Path(config_data['logger']['folder_location'])
    logger["log_filename"] = config_data['logger']['file_name']

    config["logger"] = logger

    return config
