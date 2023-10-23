import hashlib
from os import path


def get_file_hash(filename: str) -> str:
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")

    h_sha256 = hashlib.sha256()

    with open(filename, 'rb') as file:
        chunk = 0

        while chunk != b'':
            chunk = file.read(1024)
            h_sha256.update(chunk)

    return h_sha256.hexdigest()
