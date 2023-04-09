# count total even, odd number from a list using function

def even_odd(data):
    even = 0
    odd = 0

    for i in data:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b = even_odd(num)
print('Even Number : ', a)
print('Odd Number : ', b)