from logger.setup_logger import LoggerSingleton


def create_modules(config):
    modules = {}

    logger = LoggerSingleton(log_filename=config["log_filename"])
    modules["logger"] = logger

    return modules
