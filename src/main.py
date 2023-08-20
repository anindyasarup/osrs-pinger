from create_config import create_config
from create_modules import create_modules

config = create_config()
modules = create_modules(config)


def main():
    logger = modules['logger']

    logger.info("Hello, OSRS Pinger!")


if __name__ == "__main__":
    main()
