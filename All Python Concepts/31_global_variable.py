data = 5
value = 10
print('Initial Data Out side function', data)
print('Initial Value Out side function', value)

def test():
    data = 10
    print('Inside Function', data)

    global value
    value = 50
    print('Inside Value', value)

print('Before Call : ', data)
test()
print('After Call : ', data)
print('After Call : ', value)