# print a class name people where name and occupation pass into the argument
# print their occupation and name in a functon, and also say hello in another function

class People:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def work(self):
        if self.occupation == 'Actor':
            print(self.name, 'is an', self.occupation)
        elif self.occupation == 'Cricketer':
            print(self.name, 'is a', self.occupation)
        elif self.occupation == 'Footballer':
            print(self.name, 'is a', self.occupation)
        elif self.occupation == 'Student':
            print(self.name, 'is a', self.occupation)
        else:
            print(self.name, 'is a', self.occupation)

    def speak(self):
        print(self.name, 'Say Hello to YOU')

p1 = People('tuhin', 'Student')
p1.work()
p1.speak()

p2 = People('Shamim', 'Teacher')
p2.work()
p2.speak()
