class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)

    class Laptop:
        def __init__(self):
            self.name = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.name, self.cpu, self.ram)

student1 = Student('Tuhin', 1)
student2 = Student('Shanto', 2)

print(student1.name)
print(student2.name)

student1.show()
student2.show()

laptop1 = student1.laptop
laptop2 = student2.laptop

print(laptop1.name)
print(laptop2.name)

print(id(laptop1))
print(id(laptop2))

lap1 = Student.Laptop()
lap1.show()