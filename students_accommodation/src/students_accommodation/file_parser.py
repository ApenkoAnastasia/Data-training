from datetime import datetime
from collections import namedtuple
import json


def json_parser(file_path: str):
    with open(file_path, 'r') as file:
        parsed_json = json.load(file)
    return parsed_json



      # for item in parsed_json:
        #     my_date = datetime.strptime(item['birthday'], '%Y-%m-%dT%H:%M:%S.%f')
        #     print(item)
        #     print(my_date, type(my_date))


def csv_parser(file_path: str, delimiter: str):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(delimiter)


def xml_parser(file_path: str):
    pass
