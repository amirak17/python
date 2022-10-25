

print('Accessing 1D array memeber')
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])

print('\n----\n')




print('Adding 1D array memebers')
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])
print('\n----\n')




print('Accessing 2D array memeber')
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])
print('\n----\n')

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd dim: ', arr[1, 4])
print('\n----\n')




print('Accessing 3D array memeber')
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print('\n----\n')




print('Negative Indexing')
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])
