import hashlib
import logging

from os import path

logger = logging.getLogger('studentsLog')


def get_file_hash(filename: str) -> str:
    """ Receive hash of input file for trekking data loses

    :param filename: input filename
    :return: hash of file (sha256)
    """
    if path.isfile(filename) is False:
        logger.exception('File not found for hash operation.', FileNotFoundError)
        raise Exception("File not found for hash operation")

    h_sha256 = hashlib.sha256()

    with open(filename, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            h_sha256.update(chunk)

    return h_sha256.hexdigest()
