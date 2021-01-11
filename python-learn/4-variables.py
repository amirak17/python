# a variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). rules for python variables:
# a variable name must start with a letter or the underscore character
# a variable name cannot start with a number
# a variable name can only contain alpha-numeric characters and underscores (a-z, 0-9, and _ )
# variable names are case-sensitive (age, age and age are three different variables)

print('simple assignment')
x = 5
y = "john"
print(x)
print(y)
print('\n----\n')

print('new type assignment')
x = 4       # x is of type int
x = "sally" # x is now of type str
print(x)
print('\n----\n')

print('specify types')
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print('\n----\n')

print('show data type')
x = 5
y = "john"
print(type(x))
print(type(y))
print('\n----\n')

print('both types of quotes are same')
x = "john"
print(x)
# is the same as
x = 'john'
print(x)
print('\n----\n')

print('case matters')
a = 4
a = "sally"
print(a)
print(a)
#a will not overwrite a
print('\n----\n')

print('legal variable names')
myvar = "john"
my_var = "john"
_my_var = "john"
myvar = "john"
myvar = "john"
myvar2 = "john"

# many values to multiple variables
# python allows you to assign values to multiple variables in one line:
print('multiple assignment to vars')
x, y, z = "orange", "banana", "cherry"
print(x)
print(y)
print(z)
print('\n----\n')

print('single assignment to vars')
x = y = z = "orange"
print(x)
print(y)
print(z)
print('\n----\n')

print('unpack collection')
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print('\n----\n')

# you can also use the + character to add a variable to another variable:
print('plus sign to add str vars eg 1')
x = "awesome"
print("python is " + x)
print('\n----\n')

print('plus sign to add str vars eg 2')
x = "python is "
y = "awesome"
z =  x + y
print(z)
print('\n----\n')

# for numbers, the + character works as a mathematical operator:
print('plus sign to add numbers')
x = 5
y = 10
print(x + y)
print('\n----\n')

# if you try to combine a string and a number, python will give you an error:
# x = 5
# y = "john"
# print(x + y)

print('global variables eg 1')
x = "awesome"
def myfunc1():
  print("python is " + x)
myfunc1()
print('\n----\n')

print('global variables eg 2')
x = "awesome"
def myfunc2():
  x = "fantastic"
  print("python is " + x)
myfunc2()
print("python is " + x)
print('\n----\n')

print('global variables eg 3')
def myfunc3():
  global x
  x = "fantastic"
myfunc3()
print("python is " + x)
print('\n----\n')

print('change global variables inside fn')
x = "awesome"
def myfunc4():
  global x
  x = "fantastic"
myfunc4()
print("python is " + x)
print('\n----\n')
