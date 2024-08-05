import numpy as np

array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(array)
print(array[1])
print(array[2])
print(array[3])
print(array[4])
print(array[5])
print(array[6])
print(array[7])
print(array[8])

print(array[1:3])
print(array[2:4])
print(array[3:5])
print(array[4:6])
print(array[5:7])
print(array[6:8])

#Indexación booleana
bool_index = array > 50
print(bool_index)
print(type(bool_index))

#Otro ejemplo con index
index = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(index)


array = np.random.randint(1, 100, 10, size=(10))
print(array)