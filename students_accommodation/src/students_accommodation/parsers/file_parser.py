import json

from src.students_accommodation.parsers.file_hashing import get_file_hash


def json_parser(file_path: str) -> list:
    file_hash = get_file_hash(file_path)

    with open(file_path, 'r') as file:
        parsed_json = json.load(file)

    return parsed_json


def csv_parser(file_path: str, delimiter: str):
    file_hash = get_file_hash(file_path)

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(delimiter)


def xml_parser(file_path: str):
    file_hash = get_file_hash(file_path)

    # with open(file_path, 'r') as file:
