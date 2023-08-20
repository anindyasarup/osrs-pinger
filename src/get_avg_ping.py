import pinger
import process


def get_avg_ping(config, logger):
    worlds: list[int] = config['osrs']['worlds']

    for world in worlds:
        process_args = pinger.create_ping_args(logger,
                                               process_config=config['process'],
                                               host=config['osrs']['host'],
                                               world=world)

        process_object = process.create_process_object(logger, process_args)
