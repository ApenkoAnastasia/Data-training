import json


def json_parser(file_path: str) -> list:
    with open(file_path, 'r') as file:
        parsed_json = json.load(file)

    return parsed_json


def csv_parser(file_path: str, delimiter: str):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(delimiter)


def xml_parser(file_path: str):
    pass
