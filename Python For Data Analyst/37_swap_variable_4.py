a = int(input('Enter a number : '))
b = int(input('Enter another number : '))

print('A : ', a, 'B : ', b)

temp = a * b
a = temp / a
b = temp / b

print('A : ', a, 'B : ', b)
