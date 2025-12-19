import logging

import datetime

logger = logging.getLogger(__name__)

def write_log_info(msg: str):
    """Logs a message with a timestamp to the console."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f'[{timestamp}] {msg}'
    logger.info(log_message)
    print(log_message)