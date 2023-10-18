from datetime import datetime
from collections import namedtuple
import json
from src.students_accommodation.entities import *


# def customRoomDecoder(roomDict):
#     return namedtuple('X', roomDict.keys())(*roomDict.values())

def json_parser(file_path: str):
    with open(file_path, 'r') as file:
        parsed_json = json.load(file)
        for item in parsed_json:
            room_obj = Room(item['id'], item['name'])
            print(room_obj)

        # room_obj = json.load(file, object_hook=customRoomDecoder)

        # print("After Converting JSON Data into Custom Python Object")
        # my_room = Room(room_obj.room_id, room_obj.name)
        # print(my_room)

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
