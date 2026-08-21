
"Punto 4B: Realice un programa que le permita al usuario escoger entre robot cilindrico, cartesiano y esferico"
"donde como respuesta a la seleccion conteste con el tipo y numero de articulaciones que posee"

def robot():
    
    while True:
        print("\n SELECCIONE EL TIPO DE ROBOT ")
        print("1. Robot Cartesiano")
        print("2. Robot Cilindrico")
        print("3. Robot Esferico")
                
        opcion = input("Ingrese el numero que desee (1-3): ").strip()
        print()

        if opcion == "1":
            print("--- Robot Cartesiano ---")
            print(" Numero de articulaciones: 3")
            print(" Tipo de articulaciones: 3 Prismaticas")
            print(" Movimiento: Movimientos en ejes X, Y, Z (movimientos lineales).")

        elif opcion == "2":
            print("--- Robot Cilindrico ---")
            print(" Numero de articulaciones: 3")
            print(" Tipo de articulaciones: 1 Rotacional y 2 Prismaticas")
            print(" Movimiento: Rotacion en la base, elevación lineal y extension lineal.")

        elif opcion == "3":
            print("--- Robot Esferico ---")
            print(" Numero de articulaciones: 3")
            print(" Tipo de articulaciones: 2 Rotacionales y 1 Prismatica")
            print(" Movimiento: Rotacion en la base, inclinacion angular y extension lineal.")

        else:
            print("Opción no valida. Por favor seleccione 1, 2 o 3.")

        print()
        respuesta = input("¿Deseas seleccionar otra configuracion? (si/no): ").strip().lower()
        
        if respuesta != "si":
            print("Programa finalizado.")
            break

if __name__ == "__main__": robot()