import json
import logging

from src.students_accommodation.parsers.file_hashing import get_file_hash

logger = logging.getLogger('studentsLog')


def json_parser(file_path: str) -> list:
    """ Method for reading and parsing file in JSON format.

    :param file_path: path to the input file
    :return: list with receiving data
    """
    file_hash = get_file_hash(file_path)

    with open(file_path, 'r') as file:
        parsed_json = json.load(file)

    return parsed_json


def csv_parser(file_path: str, delimiter: str = ';') -> list:
    """ Method for reading and parsing file in CSV format.

    :param file_path: path to the input file
    :param delimiter: string with delimiter for parsing rows
    :return: list with receiving data
    """
    file_hash = get_file_hash(file_path)

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(delimiter)

    return data


def xml_parser(file_path: str):
    """ Method for reading and parsing file in XML format.

    :param file_path: path to the input file
    :return: list with receiving data
    """
    file_hash = get_file_hash(file_path)

    # with open(file_path, 'r') as file:
