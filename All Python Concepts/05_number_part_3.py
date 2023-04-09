# check two numbers which comes from users that are equal, not equal,
# greater than, less than, greater than equal, less than equal

a = int(input('Enter Any Number : '))
b = int(input('Enter Another Number :'))

print(a, '=', b, a == b)
print(a, '!=', b, a != b)
print(a, '>', b, a > b)
print(a, '>=', b, a >= b)
print(a, '<', b, a < b)
print(a, '<=', b, a <= b)