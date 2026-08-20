import math

# FUNCIÓN DE DEFENSA: Obliga al usuario a ingresar un número positivo real
def pedir_medida(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("  -> Error: ¡Las medidas físicas deben ser mayores a cero! Intente de nuevo.")
            else:
                return valor # Si todo está bien, devuelve el número y sale del ciclo
        except ValueError:
            print("  -> Error: Por favor, ingrese un número válido, no letras.")

# INICIO DEL PROGRAMA PRINCIPAL
print("=== CALCULADORA DE VOLÚMENES ===")
print("1. Prisma rectangular")
print("2. Pirámide rectangular")
print("3. Cono truncado")
print("4. Cilindro")

opcion = input("\nSeleccione el sólido geométrico (1-4): ")

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
    volumen = (1/3) * math.pi * h * (R**2 + R*r + r**2)
    print(f"\nEl volumen del cono truncado es: {volumen:.2f}")

elif opcion == '4':
    print("\n--- Cilindro ---")
    r = pedir_medida("Ingrese el radio del cilindro: ")
    h = pedir_medida("Ingrese la altura del cilindro: ")
    volumen = math.pi * (r**2) * h
    print(f"\nEl volumen del cilindro es: {volumen:.2f}")

else:
    print("\nOpción no válida. Por favor, reinicie el programa y elija un número del 1 al 4.")