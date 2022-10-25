
# https://www.w3schools.com/python/python_datetime.asp

print('Datetime')
print('\n----\n')

import datetime
x = datetime.datetime.now()
print(x)

print('\n----\n')




print('Format - now()')

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

print('\n----\n')




print('Specific Date')
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%B"))

print('\n----\n')
