class Room:

    def __init__(self, room_id, name):
        self.room_id = room_id
        self.name = name

    def display_info(self):
        print(f"Room name: {self.name}  ID: {self.room_id}")


class Student:

    def __init__(self, student_id, name, room, birthday, sex):
        self.student_id = student_id
        self.name = name
        self.room = room
        self.birthday = birthday
        self.sex = sex

    def display_info(self):
        print(f'Name: {self.name}  ID: {self.student_id} '
              f'Room Number: {self.room} Birthday: {self.birthday} Gender: {self.sex}')
