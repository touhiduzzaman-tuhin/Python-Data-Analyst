# find your name from your friends list if not found then print not found
friends = ['tuhin', 'fahim', 'shawon', 'sudip', 'anu', 'rana', 'shanto']

name = input('Enter Name : ')

for data in friends:
    if data == name:
        print('Found')
        break
else:
    print('Not Found')