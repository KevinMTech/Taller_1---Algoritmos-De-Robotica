import numpy as np
import matplotlib.pyplot as plt

print("=== GRÁFICA DE CIRCUITO RC (CARGA Y DESCARGA) ===")

# 1. Ingreso de datos con validación para evitar errores matemáticos
while True:
    try:
        V = float(input("Ingrese el valor de voltaje de la fuente (V): "))
        C_uF = float(input("Ingrese la capacitancia en microfaradios (uF): "))
        R = float(input("Ingrese el valor de la resistencia (Ohmios): "))
        
        # Validamos que C y R sean estrictamente positivos para evitar Tau = 0
        if C_uF <= 0 or R <= 0:
            print(" -> ¡Error físico! La Resistencia y la Capacitancia deben ser mayores a 0.")
        else:
            break # Si los datos son válidos, rompemos el ciclo y continuamos
    except ValueError:
        print(" -> Error: Por favor, ingrese valores numéricos.")

# 2. Conversiones y cálculos fundamentales
C = C_uF * 1e-6 # Convertir a Faradios
tau = R * C     # Constante de tiempo Tau

# 3. Creación del vector de tiempo (hasta 5 Tau para ver el ciclo completo)
t = np.linspace(0, 5*tau, 500)

# 4. Ecuaciones de carga y descarga
v_carga = V * (1 - np.exp(-t / tau))
v_descarga = V * np.exp(-t / tau)

# 5. Configuración de la gráfica
plt.figure(figsize=(10, 6))

plt.plot(t, v_carga, label='Carga (Sube)', color='blue', linewidth=2)
plt.plot(t, v_descarga, label='Descarga (Baja)', color='red', linewidth=2)

# Punto de cruce (opcional, pero se ve genial en la gráfica)
t_cruce = tau * np.log(2)
v_cruce = V / 2
plt.plot(t_cruce, v_cruce, 'ko', label=f'Cruce (50% V)\nt={t_cruce:.4f}s')

# Personalización
plt.title(f'Comportamiento Circuito RC\n(V={V}V, R={R}Ω, C={C_uF}uF, Tau={tau:.4f}s)')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Voltaje en el capacitor (V)')
plt.grid(True)
plt.legend()

plt.show()