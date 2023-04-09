# create a person class and print name, age, city in a function use init
# create a computer class and print name, cpu, ram in a function use init
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def show(self):
        print('Descriptions : ', self.name, self.age, self.city)

p1 =Person('tuhin', 28, 'rangpur')
print(p1.name)
p1.show()

print('\n')

class Computer:
    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config : ', self.name, self.cpu, self.ram)

c1 = Computer('HP', 'i5', 8)
print(c1.name)
c1.config()