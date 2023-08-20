from create_config import create_config
from create_modules import create_modules
from get_avg_ping import get_avg_ping

config = create_config()
modules = create_modules(config)


def main():
    logger = modules['logger']

    logger.info("Hello, OSRS Pinger!")

    rtt = get_avg_ping(config, logger)

    logger.info(rtt)


if __name__ == "__main__":
    main()
