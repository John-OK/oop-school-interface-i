from .person import Person
import csv

class Student(Person):
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self. school_id = school_id

    @classmethod
    def all_students(cls):
        students = []
        with open('../data/students.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student_data = ({
                    'name': row['name'].lower(),
                    'age': row['age'],
                    'role': row['role'].lower(),
                    'school_id': row['school_id'],
                    'password': row['password']
                })
                students.append(Student(**student_data))
        return students