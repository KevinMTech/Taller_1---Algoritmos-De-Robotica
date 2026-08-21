"""
Taller 1 - Robótica
Punto C3: Gráfica de carga y descarga de un circuito RC.
"""

import numpy as np
import matplotlib.pyplot as plt

print("=== GRÁFICA DE CIRCUITO RC (CARGA Y DESCARGA) ===")

# 1. Ingreso de datos por teclado con validación
# Usamos un while para obligar al usuario a dar valores correctos
while True:
    try:
        V = float(input("Ingrese el valor de voltaje de la fuente (V): "))
        C_uF = float(input("Ingrese la capacitancia en microfaradios (uF): "))
        R = float(input("Ingrese el valor de la resistencia (Ohmios): "))
        
        # Validamos que C y R no sean 0. Si lo fueran, Tau sería 0 y la 
        # función exponencial fallaría por división por cero.
        if C_uF <= 0 or R <= 0:
            print(" -> ¡Error físico! La Resistencia y la Capacitancia deben ser mayores a 0.")
        else:
            break # Los datos son válidos, rompemos el ciclo
    except ValueError:
        print(" -> Error: Por favor, ingrese valores numéricos.")

# 2. Cálculos fundamentales
# Multiplicamos por 1e-6 para convertir los microfaradios a Faradios estándar
C = C_uF * 1e-6 
# Calculamos la constante de tiempo Tau (tiempo que tarda en cargarse al 63.2%)
tau = R * C     

# 3. Creación del vector de tiempo
# Un capacitor se considera casi 100% cargado/descargado a los 5 Tau, 
# por eso graficamos desde 0 hasta 5*tau con 500 puntos para que la curva sea suave.
t = np.linspace(0, 5*tau, 500)

# 4. Ecuaciones matemáticas de los capacitores
v_carga = V * (1 - np.exp(-t / tau))
v_descarga = V * np.exp(-t / tau)

# 5. Configuración de la ventana y la gráfica
plt.figure(figsize=(10, 6))

# Dibujamos las dos curvas
plt.plot(t, v_carga, label='Carga', color='blue', linewidth=2)
plt.plot(t, v_descarga, label='Descarga', color='red', linewidth=2)

# Calculamos matemáticamente dónde se cruzan las líneas (al 50% del voltaje)
# Esto sirve para demostrar que la ecuación funciona perfectamente
t_cruce = tau * np.log(2)
v_cruce = V / 2
plt.plot(t_cruce, v_cruce, 'ko', label=f'Cruce (50% V)\nt={t_cruce:.4f}s')

# Textos, títulos y formato visual
plt.title(f'Comportamiento Circuito RC\n(V={V}V, R={R}Ω, C={C_uF}uF, Tau={tau:.4f}s)')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Voltaje en el capacitor (V)')
plt.grid(True)
plt.legend()

# Mostramos el resultado en pantalla
plt.show()