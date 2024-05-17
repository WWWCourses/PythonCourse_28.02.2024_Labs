import numpy as np

# # Original array with sahpe 2 rows and 3 columns (2x3)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Original array (2x3):\n", arr)

# arr3x2 = arr.reshape(3,2)
# print( arr3x2 )

# arr = np.arange(1,13)
# print( arr.reshape( (2,3,2) ))
# print( np.reshape(arr, (2,3,2) ))
# # # (2,3,2)


# arr3x2 = np.arange(1,9).reshape(3,2)

arr = np.arange(1,9)
print(arr)
arr.resize(3,4)
print(arr)