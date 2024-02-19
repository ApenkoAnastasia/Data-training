import hashlib
import logging

from os import path

logger = logging.getLogger('studentsLog')


def get_file_hash(filename: str) -> str:
    """ Receive hash of input file for trekking data loses

    :param filename: input filename
    :return: hash of file (sha256)
    """
    h_sha256 = hashlib.sha256()

    try:
        with open(filename, 'rb') as file:
            chunk = 0

            while chunk != b'':
                chunk = file.read(1024)
                h_sha256.update(chunk)
    except FileNotFoundError as err:
        logger.warning("File not found for hash operation. %s.", err, exc_info=True)

    return h_sha256.hexdigest()
