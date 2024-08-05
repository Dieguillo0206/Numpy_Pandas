import numpy as np

# Escalar: medir un solo valor (dimensión cero)
escalar = np.array(42)
print(type(escalar))
print(escalar)

# Vector: una lista de escalares (dimensión uno)
vector = np.array([1, 2, 3, 4])
print(type(vector))
print(vector)


#Matriz: una lista de vectores (dimensión dos)
#Los corchetes representan las dimensiones de la matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(matriz))
print(matriz)

#tensor: una lista de matrices (dimensión tres)
tensor = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
])
print(type(tensor))
print(tensor)

#array: una lista de tensores (dimensión n)
array_range = np.arange(27)
array = array_range.reshape((3, 3, 3))
print(type(array))
print(array)



#Matriz diagonal
matriz_diagonal = np.diag([1, 2, 3, 4])
print(type(matriz_diagonal))
print(matriz_diagonal)


#random
matriz_random = np.random.random((3, 3))
print(type(matriz_random))
print(matriz_random)