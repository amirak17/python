
print('Reshape From 1-D to 2-D')
# Convert the following 1-D array with 12 elements into a 2-D array.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # The dimension will have 4 arrays, each with 3 elements:
print(newarr)

print('\n----\n')




print('Reshape From 1-D to 3-D')
# Convert the following 1-D array with 12 elements into a 3-D array.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) # The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
print(newarr)

print('\n----\n')


# Can We Reshape Into any Shape?
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3) # Error
# print(newarr)


print('Flattening the arrays')
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

print('\n----\n')
