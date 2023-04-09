a = int(input('Enter A Number : '))
b = int(input('Enter Another Number : '))
print('A =', a, 'B =', b)

a = a * b
b = a // b
a = a // b

print('A =', a, 'B =', b)