"""
Start the pinging process of each world by creating ping arguments, executing 
the created process object from the ping arguments and sorting the ping 
key-value dictionary to get the fastest worlds for osrs. 
"""


def start_pinging(config, logger, pinger, process):
    """
    In a loop, fetches each world from the config object and then proceeds to:
        1) Create command line arguments for the selected world
        2) Create the process object using those command line arguments
        3) Executes the created process object
        4) Parses the output from the process object for avg and max 
            round-trip-time's (rtt) of the ping.

    After the loop is over, it sorts the rtt dictionary in ascending order 
    of fastest to slowest avg ping values.

    Args:
        config (_type_): config object containing key-value dictionary 
        modeling the config file 
        logger (_type_): logger singleton object
        pinger (_type_): pinger module
        process (_type_): process module 
    """
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

    rtt = pinger.sort_by_avg_ping(rtt)  # sort by avg ping in ascending order

    logger.info(rtt)
