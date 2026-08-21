import matplotlib.pyplot as plt
import numpy as np

print("--- GRAFICADOR DE VECTOR 3D ---")

try:
    # Interacción para obtener las coordenadas del vector
    x_val = float(input("Ingrese la coordenada X del vector: "))
    y_val = float(input("Ingrese la coordenada Y del vector: "))
    z_val = float(input("Ingrese la coordenada Z del vector: "))

    # Configuración inicial de la figura y el eje 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Coordenadas de origen del vector
    origen = [0, 0, 0]

    # Dibujar el vector usando quiver
    # quiver(X, Y, Z, U, V, W) donde X,Y,Z es el origen y U,V,W es la dirección/magnitud
    ax.quiver(origen[0], origen[1], origen[2], 
              x_val, y_val, z_val, 
              color='red', arrow_length_ratio=0.1, linewidth=2)

    # Determinar los límites de los ejes dinámicamente para que el vector siempre se vea bien
    limite_max = max(abs(x_val), abs(y_val), abs(z_val), 1)
    
    ax.set_xlim([-limite_max, limite_max])
    ax.set_ylim([-limite_max, limite_max])
    ax.set_zlim([-limite_max, limite_max])

    # Etiquetar ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title(f'Vector 3D: V({x_val}, {y_val}, {z_val})')

    #líneas de referencia pasando por el origen
    ax.plot([-limite_max, limite_max], [0, 0], [0, 0], color='gray', linestyle='--', linewidth=0.5)
    ax.plot([0, 0], [-limite_max, limite_max], [0, 0], color='gray', linestyle='--', linewidth=0.5)
    ax.plot([0, 0], [0, 0], [-limite_max, limite_max], color='gray', linestyle='--', linewidth=0.5)

    # Mostrar la ventana con la gráfica
    plt.show()

except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para las coordenadas.")