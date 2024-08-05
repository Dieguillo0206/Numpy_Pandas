import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array)
print(array.ndim)
print(array.shape)
print(array.dtype)


#float32
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32)
print(a)

#float64
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float64)
print(b)


a= a.astype(np.float32)
print(a)

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
suma = array.sum()
print(suma)

mean = np.mean(array)
print(mean)

std = np.std(array)
print(std)


