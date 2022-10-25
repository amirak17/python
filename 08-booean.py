
# https://www.w3schools.com/python/python_booleans.asp

print('boolean eg 1')
print(10 > 9)
print(10 == 9)
print(10 < 9)
print('\n------\n')

print('boolean eg 2')
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print('\n------\n')

print('boolean eg 3')
print(bool("Hello"))
print(bool(15))
print('\n------\n')

print('boolean eg 4')
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print('\n------\n')

print('boolean eg 5')
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print('\n------\n')

# false
print('boolean eg false')
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print('\n------\n')

print('boolean __len__')
# One more value, or object in this case, evaluates to False, and that is
# if you have an object that is made from a class with a __len__ function that
# returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
print('\n------\n')

print('Print the answer of a function')
def myFunction():
  return True
print(myFunction())
print('\n------\n')


print('You can execute code based on the Boolean answer of a function')
def myFunction():
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
print('\n------\n')


# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to determine if an object is of a certain data type:
print('isinstance')
x = 200
print(isinstance(x, int))
print(isinstance(x, float))
print('\n------\n')
