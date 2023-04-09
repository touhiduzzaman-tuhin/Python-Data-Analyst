# create a computer class and print name, cpu, ram in a function use init

class Computer:
    def __init__(self, name, cpu, ram):
        self.name = name
        self.cpu = cpu
        self.ram = ram

    def show(self):
        print('Name :', self.name)
        print('Cpu :', self.cpu)
        print('Ram :', self.ram)

c1 = Computer('Hp', 'i5', 8)
c1.show()