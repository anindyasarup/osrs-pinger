def create_process_args(logger, process_config, host, world: int):
    command: list[str] = [process_config['command'], process_config['quiet_argument'],
                          process_config['count_argument'], process_config['count']]
    host: str = host.replace('_world', str(world))

    process_args = command[:]
    process_args.append(host)

    logger.info('Created Process Arguments: %s', process_args)
    return process_args
