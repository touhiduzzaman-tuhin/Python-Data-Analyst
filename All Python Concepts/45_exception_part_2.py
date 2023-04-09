a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('Closed')

print('Last Line')