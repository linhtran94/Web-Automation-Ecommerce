import logging
import pathlib
from datetime import datetime

from utilities.getpath import get_root_folder_path


class Logger:
    """
    https://docs.python.org/3/howto/logging-cookbook.html
    https://docs.python.org/3.8/library/logging.html
    """
    pathlib.Path(get_root_folder_path() + '/logs').mkdir(parents=True, exist_ok=True)

    @staticmethod
    def logger():
        now = datetime.now()
        date_format = '%m-%d-%Y'
        file_extension = '.log'
        log_format = '%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s'

        log_file_path = get_root_folder_path() + '/logs/automated-' + now.strftime(date_format) + file_extension

        logger = logging.getLogger(__name__)

        # To override the default severity of logging
        logger.setLevel(logging.INFO)

        # Use StreamHandler() to log to console
        console_handler = logging.StreamHandler()

        # Use FileHandler() to log to a file
        file_handler = logging.FileHandler(log_file_path)

        # Set format for logging
        formatter = logging.Formatter(log_format)

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        # Add the handlers to the logger -> handlers: write to file and console
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
