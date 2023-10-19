from datetime import datetime


# class Lt_room:
#     """Room class. For saving information about rooms from .json file."""
#
#     def __init__(self, room_id: int, name: str):
#         self.room_id = int(room_id)
#         self.name = str(name)
#
#     def __str__(self):
#         return f"Room name: {self.name}  ID: {self.room_id}"


class Room(object):
    def __init__(self, id: int, name: str):
        self.room_id = int(id)
        self.name = str(name)

    def __str__(self):
        return f"Room name: {self.name}  ID: {self.room_id}, Types: {type(self.room_id)}"


class Student:
    """Student class. For saving information about students from .json file."""

    def __init__(self, student_id: str, name: str, room: str, birthday: str, sex: str):
        self.student_id = int(student_id)
        self.name = str(name)
        self.room = int(room)
        self.birthday = datetime.strptime(birthday, '%Y-%m-%dT%H:%M:%S.%f')
        self.sex = str(sex)

    def __str__(self):
        return f"Name: {self.name}  ID: {self.student_id} Room Number: {self.room} Birthday: {self.birthday} Gender: {self.sex}"
