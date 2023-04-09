print(__name__)

def calculated_area(base, height):
    area = base * height * 1/2
    return area

if '__main__' == __name__:
    result = calculated_area(5, 6)
    print(result)