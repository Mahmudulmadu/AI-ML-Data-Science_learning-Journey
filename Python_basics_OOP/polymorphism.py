class Teacher:
    def designation(self):
        print("Teacher")

class Student(Teacher):
    def designation(self):
        print("Student")

s1 = Student()
s1.designation()