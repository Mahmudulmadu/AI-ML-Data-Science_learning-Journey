class Student:

    def __init__(self, name , age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def get_cgpa(self):
        
        return self.cgpa

stu1 = Student("Mahmudul", 26,6)

print(stu1.get_cgpa(2))
        