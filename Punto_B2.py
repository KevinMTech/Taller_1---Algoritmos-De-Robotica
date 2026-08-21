import random

print("--- GENERADOR DE NÚMEROS ALEATORIOS ---")

try:
    cantidad = int(input("Ingrese la cantidad de números (X) que desea generar: "))
    limite_inf = int(input("Ingrese el límite inferior del rango: "))
    limite_sup = int(input("Ingrese el límite superior del rango: "))

    # Validación para que el rango tenga sentido
    if limite_inf > limite_sup:
        print("El límite inferior no puede ser mayor al límite superior. Invirtiendo valores...")
        limite_inf, limite_sup = limite_sup, limite_inf

    # Generación de la lista de números aleatorios (unicamente enteros)
    numeros_aleatorios = [random.randint(limite_inf, limite_sup) for _ in range(cantidad)]

    print(f"\nSe generaron los siguientes {cantidad} números aleatorios:")
    print(numeros_aleatorios)

except ValueError:
    print("Error: Por favor ingresar únicamente valores numéricos enteros.")