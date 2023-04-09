data = open('J:\Code\Python For Data Analysis\\funny_frank', 'r')
data1 = open('J:\Code\Python For Data Analysis\\total_word', 'a')

for line in data:
    print(line)
    words = line.split(' ')
    print(words)
    print(len(words))
    data1.write('Word Count : '+ str(len(words)) + ' ' + line)

data.close()
data1.close()


with open('J:\Code\Python For Data Analysis\\funny_frank', 'r') as f:
    print(f.read())

print(f.closed)