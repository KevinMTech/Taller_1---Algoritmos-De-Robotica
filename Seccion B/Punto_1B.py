# -*- coding: utf-8 -*-


# Ingreso de datos
voltaje = float(input("Ingrese el valor del voltaje (V): "))
corriente = float(input("Ingrese el valor de la corriente (A): "))

# Cálculo de la potencia
potencia = voltaje * corriente

# Mostrar el resultado
print("\n--- Resultado ---")
print(f"Voltaje: {voltaje} V")
print(f"Corriente: {corriente} A")
print(f"Potencia consumida: {potencia} W")