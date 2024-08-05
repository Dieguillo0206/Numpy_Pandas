# meses del año
# ventas de cada producto por cada mes

import numpy as np

# Primer paso - definir ventas mensuales    
months = np.array(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])

product1 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200])
product2 = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300])
product3 = np.array([300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400])


# Segundo paso: transformar los datos
media_product1 = np.mean(product1)
suma_product1 = np.sum(product1)
media_product2 = np.mean(product2)
suma_product2 = np.sum(product2)
media_product3 = np.mean(product3)
suma_product3 = np.sum(product3)

print(f'La media de ventas del producto 1 es: {media_product1}')
print(f'La suma de ventas del producto 1 es: {suma_product1}')
print(f'La media de ventas del producto 2 es: {media_product2}')
print(f'La suma de ventas del producto 2 es: {suma_product2}')
print(f'La media de ventas del producto 3 es: {media_product3}')
print(f'La suma de ventas del producto 3 es: {suma_product3}')

#Paso 3: Manipulación de datos
total_ventas = product1 + product2 + product3
promedio_ventas = np.mean(total_ventas)
meses_mas_ventas = months[np.argmax(total_ventas)]
meses_menos_ventas = months[np.argmin(total_ventas)]

print(f'El total de ventas es: {total_ventas}')
print(f'El promedio de ventas es: {promedio_ventas}')
print(f'El mes con más ventas es: {meses_mas_ventas}')
print(f'El mes con menos ventas es: {meses_menos_ventas}')


#Paso 4 - Operaciones avanzadas con NumPy
ventas_matrix = np.array([product1, product2, product3])
ventas_reshaped = ventas_matrix.reshape(36, 1)
ventas_transposed = ventas_matrix.T
print(ventas_matrix)
print(ventas_reshaped)
print(ventas_transposed)

#Invertir arrays
ventas_inverted = ventas_matrix[::-1]
ventas_flattened = ventas_matrix.flatten()

print(ventas_inverted)
print(ventas_flattened)

#Paso 5- Analisis de elementos unicos

unique_ventas, unique_counts = np.unique(ventas_matrix, return_counts=True)
print(unique_ventas)
print(unique_counts)

#Paso 6 - Indexación y Slicing

ventas_primer_trimestre = ventas_matrix[:, :3]

ventas_segundo_trimestre = ventas_matrix[:, 3:6]

ventas_tercer_trimestre = ventas_matrix[:, 6:9]

ventas_cuarto_trimestre = ventas_matrix[:, 9:12]   

print(ventas_primer_trimestre)
print(ventas_segundo_trimestre)
print(ventas_tercer_trimestre)
print(ventas_cuarto_trimestre)

meses_mas_ventas = months[np.argmax(total_ventas)]
meses_menos_ventas = months[np.argmin(total_ventas)]
print(f'El mes con más ventas es: {meses_mas_ventas}')
print(f'El mes con menos ventas es: {meses_menos_ventas}')

indices = [0, 2, 4, 6, 8, 10]
ventas_indices = total_ventas[indices]
print(ventas_indices)