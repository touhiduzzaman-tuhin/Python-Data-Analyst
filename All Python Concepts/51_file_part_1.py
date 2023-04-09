data = open('J:\Code\Python For Data Analysis\\text.txt', 'w')
data.write('I Love Bangladesh')
data.close()

data1 = open('J:\Code\Python For Data Analysis\\funny.txt', 'a')
data1.write('This is real line\n')

data2 = open('J:\Code\Python For Data Analysis\\funny_frank', 'r')
print(data2.read())
print(data2.closed)
data2.close()