class Teacher:
    def __init__(self, salary):
        self.salary = salary

    def teach(self):
        print("Teaching students...")
        

class Manager:
    def __init__(self, department):
        self.department = department

    def manage(self):
        print("Managing the department...")


class Admin(Teacher, Manager):
    def __init__(self, salary, department, role):
        Manager.__init__(self, department)  # call Manager constructor
        Teacher.__init__(self, salary)      # call Teacher constructor
         
        self.role = role

    def show_info(self):
        print(f"Role: {self.role}, Salary: {self.salary}, Dept: {self.department}")


admin = Admin(20000, "IT", "Head")
admin.show_info()