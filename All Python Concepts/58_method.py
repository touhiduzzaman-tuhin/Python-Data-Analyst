class Student:

    school = 'DIU'

    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3)/3
        return avg

    def set_marks1(self, value):
        self.marks1 = value

    def get_marks1(self):
        return self.marks1

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is static method and abc class')

student1 = Student(55, 34, 23)
student2 = Student(59, 74, 98)

print(student1.marks1)
print(student2.marks3)
print(student1.average())
print(student2.average())
print(Student.get_school())
Student.info()