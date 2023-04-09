# create a friends list and print the list
friends = ['tuhin', 'mamun', 'fahim', 'shanto', 'shawon', 'sudip', 'asif']
print(friends, type(friends))

# check 'tuhin' is on the list (using in)
print('tuhin' in friends)

# check 'Tuhin' is on the list (using in)
print('Tuhin' in friends)

# delete the last item of the list
friends.pop()
print(friends)

# delete the third last item of the list
friends.pop(3)
print(friends)

# insert 'akash' in first place of the list
friends.append('akash')
print(friends)

# insert 'mostofa' in second place of the list
friends.insert(2, 'mostofa')
print(friends)

# count total member in this list
print(len(friends))

# print the list in ascending order
friends.sort()
print(friends)

# find the position of 'shanto' in the list
pos = friends.index('fahim')
print(pos)

# change third position to 'asad' in the list
friends[2] = 'asad'
print(friends)

# create a number list then add friends and number list put it on result variable
num = [1, 4, 2, 5, 8, 3]

resutl = friends + num
print(resutl)