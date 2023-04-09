# print 1 to 10 if number is 5 then break

for i in range(1, 10):
    print(i)
    if i == 5:
        break

print('Break first then print')

for i in range(1, 10):
    if i == 5:
        break
    print(i)