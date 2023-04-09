# print a class name people where name and occupation pass into the argument
# print their occupation and name in a functon, and also say hello in another function

class People:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def work(self):
        if self.occupation == 'Student':
            print(self.name, 'is a', self.occupation)
        elif self.occupation == 'Teacher':
            print(self.name, 'is a', self.occupation)
        elif self.occupation == 'Actor':
            print(self.name, 'is a', self.occupation)
        elif self.occupation == 'Cricketer':
            print(self.name, 'is a', self.occupation)
        elif self.occupation == 'Footballer':
            print(self.name, 'is a', self.occupation)
        else:
            print(self.name, 'is a', self.occupation)

    def show(self):
        print('Hello Mr.', self.name)

p1 = People('Tuhin', 'Student')
p2 = People('Shanto', 'Data Analyst')

p1.work()
p1.show()

p2.work()
p2.show()