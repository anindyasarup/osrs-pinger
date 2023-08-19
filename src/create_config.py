from pathlib import Path
import os
import json


def create_config():
    with open('src/config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    config = {}

    config['logger_filename'] = os.path.join(Path(config_data['logger']['folder_location']),
                                             config_data['logger']['file_name'])

    return config
