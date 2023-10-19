from datetime import datetime


class Room(object):
    def __init__(self, id: int, name: str):
        self.room_id = int(id)
        self.name = str(name)

    def __str__(self):
        return f"Room name: {self.name}  ID: {self.room_id}"


class Student(object):
    """Student class. For saving information about students from .json file."""

    def __init__(self, id: str, name: str, room: str, birthday: str, sex: str):
        self.student_id = int(id)
        self.name = str(name)
        self.room = int(room)
        self.birthday = datetime.strptime(birthday, '%Y-%m-%dT%H:%M:%S.%f')
        self.sex = str(sex)

    def __str__(self):
        return (f"Name: {self.name}  ID: {self.student_id} "
                f"Room Number: {self.room} Birthday: {self.birthday} Gender: {self.sex}")
