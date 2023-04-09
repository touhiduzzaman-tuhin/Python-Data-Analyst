# print all character from a text (use for loop)
text = 'Bangladesh'

print(text)

for i in text:
    print(i)

# print all item from a list (use for loop)
list = [1, 3, 44, 5.5, 'tuhin', 3]
for i in list:
    print(i)

# print all number which divided by 5, numbers are 1 - 50
for i in range(50):
    if i % 5 == 0:
        print(i)