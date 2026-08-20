import math

print("=== CONVERSIÓN DE COORDENADAS ===")

# 1. Variables inicializadas previamente (sin input, como pide el punto A)
# Puedes cambiar estos valores para probar, incluso ponerlos en 0.
x = 2.4
y = 5.0
z = 7.2

print(f"Coordenadas Rectangulares (x, y, z): ({x}, {y}, {z})")

# 2. Conversión a Coordenadas Cilíndricas (r, theta, z)
r = math.sqrt(x**2 + y**2)
theta_cil = math.atan2(y, x) 
z_cil = z

print("\n--- Coordenadas Cilíndricas ---")
print(f"r: {r:.2f}")
print(f"Theta: {math.degrees(theta_cil):.2f} grados")
print(f"z: {z_cil:.2f}")

# 3. Conversión a Coordenadas Esféricas (rho, theta, phi)
rho = math.sqrt(x**2 + y**2 + z**2)
theta_esf = theta_cil 

# ¡AQUÍ ESTÁ LA DEFENSA! Evita la división por cero si el punto es (0,0,0)
if rho != 0:
    phi = math.acos(z / rho)
else:
    phi = 0.0

print("\n--- Coordenadas Esféricas ---")
print(f"Rho (p): {rho:.2f}")
print(f"Theta: {math.degrees(theta_esf):.2f} grados")
print(f"Phi: {math.degrees(phi):.2f} grados")