import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed_matrix = matrix.T 
print(transposed_matrix)  

array = np.arange(1, 100)
reshaped_array = array.reshape(3, 33)
print(reshaped_array)
print(array)

reversed_array = array[::-1]
print(reversed_array)
print(array)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
flattened_matrix = matrix.flatten() 
print(flattened_matrix)
print(matrix)