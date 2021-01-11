# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)


x = 5
y = "John"
print(x)
print(y)
print('----')

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
print('----')

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print('----')

x = 5
y = "John"
print(type(x))
print(type(y))
print('----')

x = "John"
print(x)
# is the same as
x = 'John'
print(x)
print('----')

a = 4
A = "Sally"
print(a)
print(A)
#A will not overwrite a
print('----')

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print('----')

x = y = z = "Orange"
print(x)
print(y)
print(z)
print('----')

# Unpack Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print('----')

# You can also use the + character to add a variable to another variable:
x = "awesome"
print("Python is " + x)
print('----')

x = "Python is "
y = "awesome"
z =  x + y
print(z)
print('----')

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
print('----')

# If you try to combine a string and a number, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

# Global Variables
x = "awesome"
def myfunc1():
  print("Python is " + x)
myfunc1()
print('----')

x = "awesome"
def myfunc2():
  x = "fantastic"
  print("Python is " + x)
myfunc2()
print("Python is " + x)
print('----')

def myfunc3():
  global x
  x = "fantastic"
myfunc3()
print("Python is " + x)
print('----')

# change the value of a global variable inside a function
x = "awesome"
def myfunc4():
  global x
  x = "fantastic"
myfunc4()
print("Python is " + x)
print('----')
