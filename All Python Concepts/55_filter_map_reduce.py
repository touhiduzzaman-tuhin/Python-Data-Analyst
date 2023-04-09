# filter

nums = [3, 5, 2, 7, 9, 11, 6, 8]

def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, nums))

print(evens)

odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

def double(n):
    return 2*n

# map

doubles = list(map(double, evens))
print(doubles)

dbl = list(map(lambda n: 2*n, evens))
print(dbl)

# reduce

from functools import reduce

def add_all(a, b):
    return a + b

sum = reduce(add_all, doubles)
print(sum)

add = reduce(lambda x, y : x + y, doubles)
print(add)