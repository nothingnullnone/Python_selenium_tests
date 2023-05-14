import logging


class Logger:
    logging.basicConfig(level="INFO")
    __logger = logging.getLogger()

    @classmethod
    def log_info(cls, message):
        cls.__logger.info(message)

    @classmethod
    def log_error(cls, message):
        cls.__logger.error(message)
