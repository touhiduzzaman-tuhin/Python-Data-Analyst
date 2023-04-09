def fibonacci_number(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)

num = int(input('Enter Any Number : '))
fibonacci_number(num)