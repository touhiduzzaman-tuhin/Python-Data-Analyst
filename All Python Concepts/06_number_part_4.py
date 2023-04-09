# use and, or, not to check condition

a = int(input('Enter A Number : '))
b = int(input('Enter Another Number : '))

print(a < b and b > 10)
print(a < b and b < 10)
print(a < b or b < 10)
print(a > b or b < 10)
print(not(a < b))
print(not(a > b))