"""
Taller 1 - Robótica
Punto A3: Conversión de coordenadas rectangulares a cilíndricas y esféricas.
Nota: Este punto es sin interacción de consola, por lo que las variables
se inicializan directamente en el código.
"""

import math

print("=== CONVERSIÓN DE COORDENADAS ===")

# 1. Inicialización de las variables rectangulares (x, y, z)
# Se pueden cambiar estos valores para probar otros puntos
x = 3.0
y = 4.0
z = 5.0

print(f"Coordenadas Rectangulares (x, y, z): ({x}, {y}, {z})")

# ==========================================
# 2. CONVERSIÓN A COORDENADAS CILÍNDRICAS
# ==========================================
# Calculamos el radio 'r' en el plano XY usando el teorema de Pitágoras
r = math.sqrt(x**2 + y**2)

# Calculamos el ángulo Theta. Usamos atan2 en lugar de atan normal 
# para que Python tenga en cuenta los signos de x e y (los cuadrantes)
theta_cil = math.atan2(y, x) 

# La altura z se mantiene igual en coordenadas cilíndricas
z_cil = z

print("\n--- Coordenadas Cilíndricas ---")
print(f"r: {r:.2f}")
# Convertimos el ángulo de radianes a grados para que sea más fácil de leer
print(f"Theta: {math.degrees(theta_cil):.2f} grados")
print(f"z: {z_cil:.2f}")

# ==========================================
# 3. CONVERSIÓN A COORDENADAS ESFÉRICAS
# ==========================================
# Calculamos Rho (la distancia desde el origen hasta el punto en 3D)
rho = math.sqrt(x**2 + y**2 + z**2)

# El ángulo Theta horizontal es el mismo que en las cilíndricas
theta_esf = theta_cil 

# Validación de seguridad: Calculamos Phi (ángulo de inclinación desde Z)
# Si rho es 0 (el punto es 0,0,0), evitamos hacer z/0 para que el programa no colapse
if rho != 0:
    phi = math.acos(z / rho)
else:
    phi = 0.0

print("\n--- Coordenadas Esféricas ---")
print(f"Rho (p): {rho:.2f}")
print(f"Theta: {math.degrees(theta_esf):.2f} grados")
print(f"Phi: {math.degrees(phi):.2f} grados")