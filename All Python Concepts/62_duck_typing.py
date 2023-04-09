class Pycharm:
    def execute(self):
        print('Compiling')
        print('Runnig')

class Myeidtor:
    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Runnig')

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Myeidtor()
lap1 = Laptop()
lap1.code(ide)