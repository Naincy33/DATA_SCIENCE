import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

print(arr1)  # [1 2 3 4 5]
print(arr2)  
# [[1 2 3]
#  [4 5 6]]np.zeros((3, 3))    # 3x3 array of zeros
print(np.ones((2, 4)))     # 2x4 array of ones
np.full((2, 2), 7)  # 2x2 array filled with 7
np.eye(4)           # 4x4 identity matrix
np.arange(1, 10, 2) # [1, 3, 5, 7, 9] (like range)
np.linspace(0, 1, 5) # [0. 0.25 0.5 0.75 1.] (evenly spaced)
