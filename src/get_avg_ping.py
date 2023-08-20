from typing import Union, List
import pinger


def get_avg_ping(config, logger, process_args: Union[str, List[str]]):
    worlds = config['osrs']['worlds']
