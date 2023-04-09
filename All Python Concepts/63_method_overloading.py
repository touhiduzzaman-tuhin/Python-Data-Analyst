class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        add = 0
        if a!=None and b!=None and c!=None:
            add = a + b + c

        elif a!=None and b!=None:
            add = a + b

        else:
            add = a

        return add

s1 = Student(55, 96)

print(s1.sum(5))

class A:

    def show(self):
        print('A is Show')

class B(A):
    pass

class C(A):
    def show(self):
        print('C is Show')

a = A()
a.show()

b = B()
b.show()

c = C()
c.show()