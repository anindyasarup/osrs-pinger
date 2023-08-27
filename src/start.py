def start_pinging(config, logger, pinger, process):
    worlds: list[int] = config['osrs']['worlds']

    rtt = {}

    for world in worlds:
        process_args = pinger.create_ping_args(logger,
                                               process_config=config['process'],
                                               host=config['osrs']['host'],
                                               world=world)

        process_object = process.create_process_object(logger, process_args)

        process_output = process.execute_process_object(logger,
                                                        process=process_object)

        avg_rtt, max_rtt = pinger.parse_ping_output(process_out=process_output)

        rtt[world] = {"avg": avg_rtt, "max": max_rtt}

    logger.info(rtt)
