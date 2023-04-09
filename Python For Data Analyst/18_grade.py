# find your grade based on your marks

marks = int(input('Enter Your Marks : '))

if (marks < 0 or marks > 100):
    print('Invalid Number')
elif (marks >= 80 and marks <= 100):
    print('A+')
elif (marks >= 70):
    print('A')
elif (marks >= 60):
    print('B')
elif (marks >= 50):
    print('C')
elif (marks >= 40):
    print('D')

else:
    print('F')