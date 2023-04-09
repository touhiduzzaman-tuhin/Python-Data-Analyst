# create a person class and print name, age, city in a function use init

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.city = city
        self.age = age

    def show(self):
        print('Name :', self.name, 'Age :', self.age, 'City :', self.city)
        print('Description : ', self.name, self.age, self.city)

p1 = Person('tuhin', 27, 'Rangpur')
print(p1.name)
p1.show()