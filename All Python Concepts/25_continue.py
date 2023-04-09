# print 1 to 10 skip 5
# print 1 to 50 skip which is divided by 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print('First continue')

for i in range(1, 20):
    if i % 5 == 0:
        continue
    print(i)
