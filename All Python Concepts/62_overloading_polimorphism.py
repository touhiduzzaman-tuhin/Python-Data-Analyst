a = 5
b = 6

print(a + b)

print(int.__add__(a,b))

a = '5'
b = '6'

print(str.__add__(a, b))


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)

        return m3

    def __gt__(self, other):
        r1 = self.m1 + self.m1
        r2 = other.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(55, 33)
s2 = Student(67, 23)

s3 = s1 + s2

print(s3)

if s1 > s2:
    print('A 1 Wins')
else:
    print('A 2 Wins')