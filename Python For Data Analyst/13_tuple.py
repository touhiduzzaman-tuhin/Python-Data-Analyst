# create a tuple and print the tuple and tuple type

tpl = (1, 2, 4, 'tuhin', 4.4, 5, 12, 'mamun', 5.5)
print(tpl, type(tpl))

# print fourth value of the tuple
print(tpl[3])

# print fourth to sixth member of the tuple
print(tpl[3:6])

# print third to last member of the tuple
print(tpl[2:])

# print fifth to last member of the tuple
print(tpl[4:])

# print last member of the tuple
print(tpl[-1])

# print reverse list
print(tpl[::-1])

# find the length of the tuple
print(len(tpl))

# find the 'tuhin' position of the tuple
print(tpl.index('tuhin'))

# count how many '3' in the tuple
print(tpl.count(3))