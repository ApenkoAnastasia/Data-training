import logging
import sys
import time
import mysql.connector as mc

logger = logging.getLogger('studentsLog')


def connect_to_mysql(config: dict, attempts=3, delay=2):
    """ Receive connection to MySQL DB.

    :param config: configurations for connection to MySQL DB
    :param attempts: number of attempts connection to DB (default=3)
    :param delay: time for waiting answer from server
    :return: connection or throw exception to log file
    """
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mc.connect(**config)
        except (mc.Error, IOError) as err:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger.error("Failed to connect, exiting without a connection: %s", err, exc_info=True)
                return None
            logger.warning(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts - 1,
            )
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
    return None
