"""
Taller 1 - Punto B.5
Escribir un programa que realice la pregunta ¿Desea continuar Si/No?
y que no deje de hacerla hasta que el usuario teclee "No".


"""

respuesta = ""

while respuesta.lower() != "no":
    respuesta = input("¿Desea continuar Si/No? ")

    if respuesta.lower() == "si":
        print("Continuando con el programa...\n")
    elif respuesta.lower() == "no":
        print("Programa finalizado. ¡Hasta luego!")
    else:
        print("Respuesta no válida. Por favor escriba 'Si' o 'No'.\n")
