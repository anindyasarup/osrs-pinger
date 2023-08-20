from typing import Union, List
import pinger


def get_avg_ping(config, logger):
    worlds: list[int] = config['osrs']['worlds']

    process_config: dict = config['process']
    command: list[str] = [process_config['command'], process_config['quiet_argument'],
                          process_config['count_argument'], process_config['count']]

    for world in worlds:
        host: str = config['osrs']['host'].replace('_world', str(world))
        process_args = command[:]
        process_args.append(host)
