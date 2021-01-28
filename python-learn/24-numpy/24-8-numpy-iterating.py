
print('Iterating Arrays')

# Iterating means going through elements one by one.

import numpy as np
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

print('\n----\n')



#
print('Iterating 2-D Arrays in One Dimension')

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

print('\n----\n')




print('Iterating 2-D Arrays in Two Dimensions Separately')

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print('--')
  for y in x:
    print(y)

print('\n----\n')


print('Iterating 3-D Arrays')

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

print('\n----\n')




print('Iterating Arrays Using nditer()')
print('Iterating 3D Array Using nditer() with single for loop')

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

print('\n----\n')




print('Iterating Array With Different Data Types')

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some
# other space to perform this action, that extra space is called buffer,
# and in order to enable it in nditer() we pass flags=['buffered'].

import numpy as np
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

print('\n----\n')




print('Iterating With Different Step Size')

# We can use filtering and followed by iteration.
# Iterate through every scalar element of the 2D array skipping 1 element:

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)


print('\n----\n')




print('Enumerated Iteration Using ndenumerate()')

# Enumeration means mentioning sequence number of somethings one by one.
#
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method
# can be used for those usecases.
#
# Enumerate on following 1D arrays elements:

import numpy as np
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

# Example
# Enumerate on following 2D array's elements:

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
