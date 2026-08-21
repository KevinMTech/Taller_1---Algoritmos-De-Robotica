"""
Taller 1 - Robótica
Punto B3: Cálculo de volúmenes con interacción de consola.
"""

import math

# Función auxiliar para validar los datos que ingresa el usuario.
# Esto evita que el programa falle si meten letras o números negativos.
def pedir_medida(mensaje):
    while True:
        try:
            # Intentamos convertir lo que ingresa el usuario a decimal (float)
            valor = float(input(mensaje))
            # Físicamente una distancia no puede ser negativa o cero
            if valor <= 0:
                print("  -> Error: ¡Las medidas deben ser mayores a cero! Intente de nuevo.")
            else:
                return valor # Si el dato es correcto, lo retornamos y salimos del ciclo
        except ValueError:
            # Si el usuario escribe texto (ej: "cinco"), atrapamos el error
            print("  -> Error: Por favor, ingrese un número válido, no letras.")

# Menú principal del programa
print("=== CALCULADORA DE VOLÚMENES ===")
print("1. Prisma rectangular")
print("2. Pirámide rectangular")
print("3. Cono truncado")
print("4. Cilindro")

opcion = input("\nSeleccione el sólido geométrico (1-4): ")

# Estructura de control para calcular el volumen según la opción elegida
if opcion == '1':
    print("\n--- Prisma Rectangular ---")
    l = pedir_medida("Ingrese el largo de la base: ")
    w = pedir_medida("Ingrese el ancho de la base: ")
    h = pedir_medida("Ingrese la altura del prisma: ")
    volumen = l * w * h
    print(f"\nEl volumen del prisma es: {volumen:.2f}")

elif opcion == '2':
    print("\n--- Pirámide Rectangular ---")
    l = pedir_medida("Ingrese el largo de la base: ")
    w = pedir_medida("Ingrese el ancho de la base: ")
    h = pedir_medida("Ingrese la altura de la pirámide: ")
    volumen = (1/3) * (l * w) * h
    print(f"\nEl volumen de la pirámide es: {volumen:.2f}")

elif opcion == '3':
    print("\n--- Cono Truncado ---")
    R = pedir_medida("Ingrese el radio mayor (R): ")
    r = pedir_medida("Ingrese el radio menor (r): ")
    h = pedir_medida("Ingrese la altura del cono truncado: ")
    # Aplicamos la fórmula matemática del cono truncado
    volumen = (1/3) * math.pi * h * (R**2 + R*r + r**2)
    print(f"\nEl volumen del cono truncado es: {volumen:.2f}")

elif opcion == '4':
    print("\n--- Cilindro ---")
    r = pedir_medida("Ingrese el radio del cilindro: ")
    h = pedir_medida("Ingrese la altura del cilindro: ")
    volumen = math.pi * (r**2) * h
    print(f"\nEl volumen del cilindro es: {volumen:.2f}")

else:
    # Por si el usuario digita un número que no está en el menú
    print("\nOpción no válida. Por favor, reinicie el programa y elija un número del 1 al 4.")