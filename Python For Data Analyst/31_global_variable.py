a = 5
b = 10

print('A : ', a)
print('B : ', b)

def test():
    a = 10
    print('A : ', a)

    global b
    b = 20
    print('B : ', b)

print('A : ', a)

test()

print('A : ', a)
print('B : ', b)