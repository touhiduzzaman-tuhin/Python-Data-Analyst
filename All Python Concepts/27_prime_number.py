# check the number is prime or not

num = int(input('Enter A Number : '))

for i in range(2, num):
    if num % i == 0:
        print('Not Prime')
        break
else:
    print('Prime Number')