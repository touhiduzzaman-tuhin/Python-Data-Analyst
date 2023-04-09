class Computer:
    pass

com1 = Computer()
com2 = Computer()

print(id(com1))
print(id(com2))

class Person:
    def __init__(self):
        self.name = 'Tuhin'
        self.age = 27

    def update(self):
        self.age = 30

    def compare(self, person2):
        if self.age == person2.age:
            print('Same Age')
        else:
            print('Not Same Age')

person1 = Person()
person2 = Person()
person3 = Person()
print(person1.name)
print(person2.name)

person3.name = 'Rana'
print(person3.name)
print(person3.age)

person3.update()
print(person3.age)

person3.compare(person2)