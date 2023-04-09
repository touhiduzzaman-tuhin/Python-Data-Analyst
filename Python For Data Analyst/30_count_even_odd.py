# count total even, odd number from a list using function
def even_odd(number):
    e = 0
    o = 0

    for i in number:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o

num = [1, 2, 5, 6, 4, 9, 23, 53, 21, 56, 34]

a, b = even_odd(num)

print('Even:', a, 'Odd:', b)
