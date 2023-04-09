# print 1 to 10 skip 5
for i in range(11):
    if i == 5:
        continue
    print(i)

# print 1 to 50 skip which is divided by 5

for i in range(51):
    if i % 5 == 0:
        continue
    print(i)
