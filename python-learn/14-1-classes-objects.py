print('Create a Class')
# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

# create object p1
p1 = MyClass()
print(p1.x)

print('\n----\n')



print('The __init__() Function')
# The __init__() function is called automatically every time the class is being used to create a new object.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print('\n----\n')




print('Object Methods')
# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

print('\n----\n')



print('The self Parameter may have its name')
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# Use the words myobject or abc etc instead of self:

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print('\n----\n')




print('Modify Object Properties')
# You can modify properties on objects like this:
p1.age = 40

print('\n----\n')

print('Delete Object Properties')
# You can delete properties on objects by using the del keyword:
del p1.age

print('\n----\n')



print('Delete Objects')
# You can delete objects by using the del keyword:
# Delete the p1 object:
del p1


print('\n----\n')




print('The pass Statement')
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example
class Person:
  pass

print('\n----\n')
