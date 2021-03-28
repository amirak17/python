
print('\n----\n')

print('functions')

def my_function():
  print("Hello from a function")
my_function()

print('\n----\n')


print('Arguments')
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print('\n----\n')



print('Number of Arguments')
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

print('\n----\n')



print('Arbitrary Arguments, *args')

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

print('\n----\n')



print('Keyword Arguments: You can also send arguments with the key = value syntax')


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print('\n----\n')


print('Arbitrary Keyword Arguments, **kwargs - for dictionary of arguments')

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")




print('argument default value')

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


print('\n----\n')




print('Passing a List as an Argument')

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print('\n----\n')



print('Return Value')

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print('\n----\n')



print('The pass Statement')

def myfunction():
  pass

print('\n----\n')




print('Recursion')

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

print('\n----\n')





print('Lambda Function eg 1')

x = lambda a, b : a * b
print(x(5, 6))

print('\n----\n')




print('Lambda Function eg 2')

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

print('\n----\n')




print('Global variables')
x = 300

def myfunc():
  global x
  print(x)
  x = 200

myfunc()
print(x)

print('\n----\n')
