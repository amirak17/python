
"""
NumPy Data Types
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

Checking the Data Type of an Array
The NumPy array object has a property called dtype that returns the data type of the array:

"""



print('NumPy Data Types')
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)


import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
print('\n----\n')




print('User Defined Data Type')
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
print('\n----\n')


print('For i, u, f, S and U we can define size')
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
print('\n----\n')




print('if a value can not be converted then numpy will raise a valueerror')
# A non integer string like 'a' can not be converted to integer (will raise an error):
# import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i')
print('\n----\n')




print('Converting Data Type on Existing Arrays Using astype()')
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print('\n----\n')




print('Change data type from float to integer by using int as parameter value')
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
print('\n----\n')

import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
print('\n----\n')
