import numpy as np

# Matrices previamente inicializadas
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Suma
suma = A + B

# Resta
resta = A - B

# Multiplicación elemento a elemento
multiplicacion = A * B

# Producto punto
producto_punto = np.dot(A, B)

# División elemento a elemento
division = A / B

# Vectores de 3 dimensiones para producto cruz
vector_A = np.array([1, 2, 3])
vector_B = np.array([4, 5, 6])

# Producto cruz
producto_cruz = np.cross(vector_A, vector_B)

# Mostrar resultados
print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

print("\nSuma:")
print(suma)

print("\nResta:")
print(resta)

print("\nMultiplicación elemento a elemento:")
print(multiplicacion)

print("\nProducto punto:")
print(producto_punto)

print("\nDivisión:")
print(division)

print("\nVector A:")
print(vector_A)

print("\nVector B:")
print(vector_B)

print("\nProducto cruz:")
print(producto_cruz)