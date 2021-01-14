
print('\n----\n')
print('Module')
import mymodule
# You can name the module file whatever you like, but it must have the file extension .py

mymodule.greeting("Jonathan")
# Note: When using a function from a module, use the syntax: module_name.function_name.

print('\n----\n')

print('Variables in Module')
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

import mymodule

a = mymodule.person1["age"]
print(a)

print('\n----\n')




print('Re-naming a Module')
import mymodule as mx

a = mx.person1["age"]
print(a)

print('\n----\n')




print('Built-in Modules')
# There are several built-in modules in Python, which you can import whenever you like.

import platform

x = platform.system()
print(x)

print('\n----\n')

# Using the dir() Function. The dir() function can be used on all modules, also the ones you create yourself.
x = dir(platform)
print(x)

print('\n----\n')




print('Import From Module')
# You can choose to import only parts from a module, by using the from keyword.

from mymodule import person1

print(person1["age"])

print('\n----\n')
