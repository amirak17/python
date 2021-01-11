
# https://www.w3schools.com/python/python_booleans.asp

def prline():
    print('\n------\n')


print(10 > 9)
print(10 == 9)
print(10 < 9)
prline()

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
prline()

print(bool("Hello"))
print(bool(15))
prline()

x = "Hello"
y = 15
print(bool(x))
print(bool(y))
prline()

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
prline()

# false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
prline()

# One more value, or object in this case, evaluates to False, and that is
# if you have an object that is made from a class with a __len__ function that
# returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
prline()

# Print the answer of a function:
def myFunction() :
  return True
print(myFunction())
prline()


# You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
prline()


# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
print(isinstance(x, float))
prline()
