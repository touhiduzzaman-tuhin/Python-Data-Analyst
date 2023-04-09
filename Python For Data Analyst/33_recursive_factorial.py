def recursive_factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * recursive_factorial(num-1)


n = int(input('Enter Any Number : '))
res = recursive_factorial(n)
print('Result : ', res)