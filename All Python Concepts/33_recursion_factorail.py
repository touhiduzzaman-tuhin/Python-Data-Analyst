def recursion_factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * recursion_factorial(num-1)

num = int(input('Enter Any Number : '))
result = recursion_factorial(num)
print('Factorial Value : ', result)