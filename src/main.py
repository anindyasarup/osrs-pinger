from create_config import create_config
from create_modules import create_modules
from start import start_pinging

config = create_config()
modules = create_modules(config)


def main():
    logger = modules['logger']

    logger.info("Hello, OSRS Pinger!")

    start_pinging(config, logger,
                  pinger=modules['pinger'],
                  process=modules['process'])


if __name__ == "__main__":
    main()
