# find different type of error like name error, value error,
# zero division error and other type of error for divide tow number

a = input('Enter a Number : ')
b = input('Enter another Number : ')

try:
    print(int(a)/int(b))
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except NameError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('Clossed')