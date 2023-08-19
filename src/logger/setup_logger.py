import logging


class LoggerSingleton:
    _instance = None
    _logger = None

    def __new__(cls, log_filename):
        if cls._instance is None:
            cls._instance = super(LoggerSingleton, cls).__new__(cls)
            cls._logger = cls._instance._configure_logger(log_filename)

        return cls._logger

    def _configure_logger(self, log_filename):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s ||> %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)

        self._logger.addHandler(console_handler)
        self._logger.addHandler(file_handler)

        return self._logger
