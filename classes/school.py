from .staff import Staff
from .student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Student.all_students
        self.students = Staff.all_staff