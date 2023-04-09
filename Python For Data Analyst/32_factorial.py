# find factorial using loop in function

def factorial_number(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

n = int(input('Enter a number : '))

result = factorial_number(n)
print(result)

