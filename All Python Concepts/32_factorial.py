def factorial_number(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

num = int(input('Enter Any Number : '))
result = factorial_number(num)
print('Factorial value :', result)
