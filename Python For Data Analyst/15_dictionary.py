# create a student details dictionary then print it and it's type
student ={
    'name': 'tuhin',
    'city': 'rangpur',
    'country': 'bangladesh',
    'institute': 'diu',
    'cgpa': 3.86,
    'friends': ['shawon', 'shanto', 'asif', 'sudip'],
    'school': {
        '1-10': ['jn', 'nasu-mamud'],
        '11-16': ['rgc', 'diu']
    }
}
print(student, type(student))

# print the items of students
print(student.items())

# print the keys of students
print(student.keys())

# print the values of students
print(student.values())

# find information from student details
print(student['name'])
print(student['city'])
print(student['cgpa'])

# find information from list from student details
print(student['school'])
# find information from list then another list from student details
print(student['school']['1-10'])

# find information from student details using get function
print(student.get('name'))

# update information from students and check
student['name'] = 'Touhiduzzaman'
print(student.get('name'))