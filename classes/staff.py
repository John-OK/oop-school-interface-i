from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff = []
        with open('../data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_data = ({
                    'name': row['name'].lower(),
                    'age': row['age'],
                    'role': row['role'].lower(),
                    'employee_id': row['employee_id'],
                    'password': row['password']
                })
                staff.append(Staff(**employee_data))
        return staff


# all = Staff.all_staff()
# print(all)
