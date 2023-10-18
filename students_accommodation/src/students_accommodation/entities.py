from datetime import datetime


class Room:
    """Room class. For saving information about rooms from .json file."""

    def __init__(self, room_id: int, name: str):
        self.room_id = int(room_id)
        self.name = str(name)

    def display_info(self):
        print(f"Room name: {self.name}  ID: {self.room_id}")


class Student:
    """Student class. For saving information about students from .json file."""

    def __init__(self, student_id: int, name: str, room: int, birthday: datetime, sex: str):
        self.student_id = int(student_id)
        self.name = str(name)
        self.room = int(room)
        self.birthday = datetime.strftime(birthday, '%Y-%m-%dT%H:%M:%S')
        self.sex = str(sex)

    def display_info(self):
        print(f"Name: {self.name}  ID: {self.student_id} "
              f"Room Number: {self.room} Birthday: {self.birthday} Gender: {self.sex}")
