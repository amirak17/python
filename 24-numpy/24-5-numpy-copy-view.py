
print('Copy')

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() # The copy SHOULD NOT be affected by the changes made to the original array.
arr[0] = 42

print(arr)
print(x)
print('\n----\n')



print('View')

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view() # The view SHOULD be affected by the changes made to the original array.
arr[0] = 42

print(arr)
print(x)
print('\n----\n')




print('Base')
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

print('\n----\n')
