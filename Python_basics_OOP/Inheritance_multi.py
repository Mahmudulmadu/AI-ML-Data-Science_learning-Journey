class Teacher:
    def __init__(self, salary, subject):
        self.salary = salary
        self.subject = subject

class Admin(Teacher):
    def __init__(self, role, salary):
        super().__init__(salary, subject=None)
        self.role  = role
class Accountant(Admin):
    def __init__(self, pos, salary, role):
        super().__init__(salary, role)
        

        self.pos = pos

ac1  = Accountant("manager",10000, "chief")


print(ac1.pos, ac1.role, ac1.salary)