# find your name from your friends list if not found then print not found

friends = ['tuhin', 'shanto', 'shawon', 'istiyak', 'juyel', 'shahed']

name = input('Enter Your Search name : ')

for i in friends:
    if i == name:
        print('Found')
        break
else:
    print('Not Found')