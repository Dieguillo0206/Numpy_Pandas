import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
suma = A + B

print(A)
print(B)
print(suma)


#Multiplicación de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
multiplicacion = A.dot(B)
print(multiplicacion)


A = np.array([[1, 2, 3], [4, 5, 6]])
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print(A)
print(det_A)
print(inv_A)

#Ax = B
D = np.array([[2, 3], [5, 7]])
E = np.array([5, 10])
X = np.linalg.solve(D, E)
print(D)
print(E)
print(X)
