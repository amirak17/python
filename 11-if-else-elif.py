"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
"""

print('if statement')
a = 33
b = 200
if b > a:
  print("b is greater than a")

print('\n----\n')

# if statement, without indentation (will raise an error):
a = 33
b = 200
# if b > a:
# print("b is greater than a") # you will get an error

print('\n----\n')

print('elif')
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print('\n----\n')

print('if elif else')
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

print('\n----\n')

print('if > else')
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print('\n----\n')

print('short hand if')
if a > b: print("a is greater than b")

print('\n----\n')

print('one line if else statement')
a = 2
b = 330
print("A") if a > b else print("B")

print('\n----\n')


print('ternary operators, or conditional expressions')
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print('\n----\n')

print('and')
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print('or')
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print('\n----\n')

print('nested if')
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print('\n----\n')

print('the pass statement')

a = 33
b = 200
if b > a:
  pass
