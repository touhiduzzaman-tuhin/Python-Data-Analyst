# create a set then print it and it's type
# delete the first value of this set
# add '9' in the last of this set
# find the length of this set
# remove 'tuhin' of this list

num = {3, 4, 2, 4, 5, 7, 8, 'tuhin', 5.5}

print(num, type(num))

num.pop()
print(num)

num.add(9)
print(num)

print(len(num))

num.remove('tuhin')
print(num)

