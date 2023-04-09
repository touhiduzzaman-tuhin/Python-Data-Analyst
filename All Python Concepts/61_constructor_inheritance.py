class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1 is working')

    def feature2(self):
        print('Feature 2 is working')


class B(A):

    def __init__(self):
        super().__init__()
        print('in B init')

    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')


class C:

    def __init__(self):
        print('in C init')

    def feature4(self):
        print('Feature 4 is working')

    def feature5(self):
        print('Feature 5 is working')

class D(A, C):

    def __init__(self):
        super().__init__()
        print('in D init')

a1 = A()
b1 = B()
c1 = C()
d1 = D()