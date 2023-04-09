# find your grade based on your marks

marks = int(input('Enter Your Marks : '))

if (marks < 40):
    print('F')
elif(marks < 50):
    print('D')
elif(marks < 60):
    print('C')
elif(marks < 70):
    print('B')
elif(marks < 80):
    print('A')
elif(marks <= 100):
    print('A+')
else:
    print('Invalid Marks')