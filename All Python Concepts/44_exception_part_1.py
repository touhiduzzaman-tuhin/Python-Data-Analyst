a = int(input('Enter any Number : '))
b = int(input('Enter another Number : '))

try:
    res = a / b
except Exception as e:
    print(e)
    res = None

print(res)