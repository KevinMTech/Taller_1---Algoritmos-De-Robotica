"""
Taller 1 - Punto A.1
Programa que suma, resta, multiplica
y divide dos vectores previamente inicializados.

"""

import numpy as np

v1 = np.array([4, -2, 7])
v2 = np.array([1, 5, 3])

print("Vector 1:", v1)
print("Vector 2:", v2)
print("-" * 40)

suma = v1 + v2
print("Suma (v1 + v2):", suma)


resta = v1 - v2
print("Resta (v1 - v2):", resta)

producto_punto = np.dot(v1, v2)
print("Producto punto (v1 · v2):", producto_punto)

producto_cruz = np.cross(v1, v2)
print("Producto cruz (v1 x v2):", producto_cruz)

division = v1 / v2
print("División (v1 / v2):", division)
