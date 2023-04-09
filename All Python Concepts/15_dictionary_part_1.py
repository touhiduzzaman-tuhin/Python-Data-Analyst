# create a student details dictionary then print it and it's type
# print the items of students
# print the keys of students
# print the values of students
# find information from student details
# find information from list from student details
# find information from list then another list from student details
# find information from student details using get function
# update information from students and check


student = {
    'name': 'tuhin',
    'age': 28,
    'city': 'Rangpur',
    'country': 'Bangladesh',
    'university': 'DIU',
    'cgpa': 3.86,
    'friends': ['shanto', 'istiyak', 'rustom', 'shawon', 'maruf'],
    'hobby': {
        'programming': ['python', 'c', 'power bi', 'sql'],
        'playing': ['cricket', 'football']
    }
}
print(student, type(student))
print(student.items())
print(student.keys())
print(student.values())
print(student['cgpa'])
print(student['hobby'])
print(student['hobby'])
print(student['hobby']['playing'])
print(student['hobby']['playing'][1])
print(student.get('friends'))
print(student.get('income'))
print(student.get('income', 'Not Found'))

student['city'] = 'Dhaka'
print(student.get('city'))