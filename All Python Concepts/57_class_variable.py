class Car:

    wheels = 4
    sit = 6

    def __init__(self):
        self.milage = 10
        self.name = "BMW"

c1 = Car()
c2 = Car()

c1.milage = 55

Car.sit = 9

print(c1.name, c1.milage, c1.sit, c1.wheels)
print(c2.name, c2.milage, c2.sit, c2.wheels)