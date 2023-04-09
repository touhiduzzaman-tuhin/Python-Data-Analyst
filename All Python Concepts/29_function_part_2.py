# write a function add two number
# write a function double a number
# write a function to calculate tri-angle area
# write a function to calculate square area


def add(a, b):
    res = a + b
    print(res)

add(5, 6)

def double(a):
    res = a * 2
    return res

res = double(5)
print(res)

def triangle_area(a, b):
    res = a * b * .5
    return res

result = triangle_area(5, 6)
print(result)

def square_area(a):
    res = a * a
    print(res)

square_area(5)