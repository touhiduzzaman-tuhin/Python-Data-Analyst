from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print('Running')


class Programmer:

    def working(self, com):
        print('Solving Bugs')
        com.process()

com1 = Laptop()
# com1.process()

programmer1 = Programmer()
programmer1.working(com1)
