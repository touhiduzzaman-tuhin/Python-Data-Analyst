# print all module form calendar
# print the type name of calendar
# print the december 2020 calendar
# check 2008, 2010, 2014, 2020 is leap year

import calendar

print(dir(calendar))
print(type(calendar))
print(calendar.month(2022, 1))
print(calendar.isleap(2020))
print(calendar.isleap(2016))
print(calendar.isleap(2008))
print(calendar.isleap(2014))
