# print 0 to 9
# print 0 to 10
# print 0 to 10 Even Number
# print 0 to 10 Odd Number
# print 0 to 10 Even Number (use if)
# print 0 to 10 Odd Number (use if)

print('0 to 9')
for i in range(10):
    print(i)

print('1 to 10')
for i in range(1, 11):
    print(i)

print('0 to 10 Even Number')
for i in range(0, 10, 2):
    print(i)

print('1 to 10 Odd Number')
for i in range(1, 10, 2):
    print(i)

print('1 t0 10 Even If')
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print('1 to 10 Odd if')
for i in range(1, 11):
    if i % 2 != 0:
        print(i)