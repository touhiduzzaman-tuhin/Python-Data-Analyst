import calendar

# print all module form calendar
print(dir(calendar))

# print the type name of calendar
print(type(calendar))

# print the december 2020 calendar
print(calendar.month(2020, 12))

# check 2008, 2010, 2014, 2020 is leap year
print(calendar.isleap(2008))
print(calendar.isleap(2010))
print(calendar.isleap(2014))
print(calendar.isleap(2020))