# create a friends list and print the list
# check 'tuhin' is on the list (using in)
# check 'Tuhin' is on the list (using in)
# delete the last item of the list
# delete the third last item of the list
# insert 'akash' in first place of the list
# insert 'mona' in second place of the list
# count total member in this list
# print the list in ascending order
# find the position of 'shanto' in the list
# change third position to 'asad' in the list
# create a number list then add friends and number list put it on result variable

friends = ['tuhin', 'fahim', 'shawon', 'sudip', 'anu', 'rana', 'shanto']

print('tuhin' in friends)
print('Tuhin' in friends)

print(friends)

print(friends.pop())
print(friends)

print(friends.pop(3))
print(friends)

friends.insert(2, 'akash')
print(friends)

friends.sort()
print(friends)

friends.append('munira')
print(friends)

print(friends.index('rana'))

print(len(friends))

friends[2] = 'mamun'
print(friends)

num = [1, 2, 3, 4, 5]

res = friends + num
print(res)