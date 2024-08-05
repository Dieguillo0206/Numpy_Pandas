import numpy as np

prices = np.array([10, 20, 30])
discount = np.array([0.25])
discount_prices = prices * (1 - discount)
print(discount_prices)  # [ 7.5 15.  22.5]

price2 = np.array([[10, 20, 30], [40, 50, 60]])
discount2 = np.array([1,2,3])
discount2 = price2 * (1 - discount2)
print(discount2)

array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(array1, axis=0)) 

array2 = np.array([1, 2, 3])
print(array1 + array2)  

concatenaded = np.concatenate((array1, [array2]), axis=0)
print(concatenaded)


stacked = np.stack((array1, array2), axis=0)
print(stacked)

stacked_v = np.stack((array1, array2), axis=1)
print(stacked_v)

array_c = np.array([[1, 2, 3], [4, 5, 6]])
split = np.split(array_c, 2, axis=0)
print(split)

array_d = np.array([[7, 8, 9], [10, 11, 12]])
split2 = np.split(array_d, 3, axis=1)
print(split2)