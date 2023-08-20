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

    logger = {}
    logger['log_folder'] = Path(config_data['logger']['folder_location'])
    logger['log_filename'] = config_data['logger']['file_name']

    process = {}
    process['command'] = config_data['process']['command']
    process['quiet_argument'] = config_data['process']['quiet_argument']
    process['count_argument'] = config_data['process']['count_argument']
    process['count'] = config_data['process']['count']

    osrs = {}
    osrs['worlds'] = config_data['osrs']['worlds']
    osrs['host'] = config_data['osrs']['host']

    config = {}
    config['logger'] = logger
    config['process'] = process
    config['osrs'] = osrs

    return config
