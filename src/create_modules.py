from logger.setup_logger import LoggerSingleton


def create_modules(config):
    modules = {}

    logger = LoggerSingleton(log_folder=config['logger']['log_folder'],
                             log_filename=config['logger']['log_filename'])

    modules['logger'] = logger

    return modules
