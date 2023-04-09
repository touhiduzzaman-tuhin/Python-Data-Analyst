# print all character from a text (use for loop)
# print all item from a list (use for loop)
# print all number which divided by 5, numbers are 1 - 50

text = 'Bangladesh'
print(text)

for i in text:
    print(i)

data = ['tuhin', 'akash', 'mona', 'aka', 1, 5, 44, 5.5, ['tania', 'sakil', 5], 'rana']
print(data)
for i in data:
    print(i)

print('1 to 30 divided by 5')
for i in range(1, 31):
    if i % 5 == 0:
        print(i)

