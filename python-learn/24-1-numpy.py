"""

NumPy is an open source library that stands for Numerical Python and is used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

This behavior is called locality of reference in computer science.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

NumPy is a Python library and is written partially in Python,
but most of the parts that require fast computation are written in C or C++.

NumPy Codebase is located at this github repository https://github.com/numpy/numpy

NumPy was initially created in 2005 by Travis Oliphant.

Install using pip3:
pip3 install numpy

"""

print('Create a NumPy ndarray Object')
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print('\n----\n')



# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
# and it will be converted into an ndarray:

# Example
# Use a tuple to create a NumPy array:

import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)



print('Dimensions in Arrays')
# A dimension in arrays is one level of array depth (nested arrays).

print('0-D Arrays')

import numpy as np
arr = np.array(42)
print(arr)

print('\n----\n')

print('1-D Arrays')



import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print('\n----\n')




print('2-D Arrays')
import numpy as np
arr = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
print(arr)

print('\n----\n')




print('3-D arrays')
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

print('\n----\n')




print('Check Number of Dimensions')

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('\n----\n')




print('Higher Dimensional Arrays')

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

print('\n----\n')
