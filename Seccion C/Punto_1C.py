
"Punto C1:Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C"

import numpy  
import matplotlib.pyplot as plt

# 1. Parámetros del sensor PT100 
R0 = 100.0          # Resistencia a 0 °C (100 Ohms)
A = 3.9083e-3       # Coeficiente A (°C^-1)
B = -5.775e-7       # Coeficiente B (°C^-2)
C = -4.183e-12      # Coeficiente C (°C^-4, solo para T < 0 °C)
 
# 2. Formula
def pt100_Resistencia(temp):
    "Se calcula la resistencia de la PT100 segun la temperatura"
    temp = numpy.array(temp)
    
    # R(T) para T >= 0 °C
    R_pos = R0 * (1 + A * temp + B * (temp ** 2))
    
    # R(T) para T < 0 °C
    R_neg = R0 * (1 + A * temp + B * (temp ** 2) + C * (temp - 100) * (temp ** 3))
    
    # Selecciona la ecuacion según el valor de T
    return numpy.where(temp >= 0, R_pos, R_neg)

# 3. Rango de temperatura de -200 °C a 200 °C 
temperaturas = numpy.linspace(-200, 200, 500)
resistencias = pt100_Resistencia(temperaturas)

# 4. Grafica
plt.figure(figsize=(10, 6))

# Curva principal
plt.plot(temperaturas, resistencias, color='blue', linewidth=2.5, label='Comportamiento PT100')

# Puntos de referencia clave
puntos = [-200, 0, 200]
for t in puntos:
    r = pt100_Resistencia(t)
    plt.plot(t, r, 'ro', markersize=6)
    plt.annotate(f'{t}°C: {r:.2f} $\Omega$', 
                 xy=(t, r), 
                 xytext=(t + 5, r - 12 if t == 200 else r + 5),
                 fontsize=9,
                 fontweight='bold',)
                 

# Configuracion visual 
plt.title('Comportamiento de la Resistencia de la PT100 (-200°C a 200°C)', fontsize=14, pad=15)
plt.xlabel('Temperatura (°C)', fontsize=12)
plt.ylabel('Resistencia ($\Omega$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()

# Mostrar la grafica
plt.show()