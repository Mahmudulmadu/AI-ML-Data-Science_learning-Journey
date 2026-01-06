class Employee:
    start_time = "10 am"
    end_time = "6 pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time


class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class Admin(Employee):
    def __init__(self, role):
        self.role =  role

t1 = Teacher("Math")

print(t1.start_time, t1.end_time, t1.subject)