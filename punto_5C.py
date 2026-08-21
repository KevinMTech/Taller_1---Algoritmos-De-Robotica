
"Punto 5C: Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D"
"Teniendo en cuenta lineas rectas y/o curvas"

import matplotlib.pyplot as plt

def dibujar_nombres():
    fig, axes = plt.subplots(5, 1, figsize=(9, 10))
    fig.suptitle("Nombres Dibujados con Líneas Rectas y Curvas", fontsize=14, fontweight='bold')

    # 1. KEVIN 
    ax = axes[0]
    # K 
    ax.plot([0, 0], [0, 2], color='red', lw=3)          # Linea recta
    ax.plot([0, 0.8], [1, 2], color='red', lw=3)        # Diagonal arriba
    ax.plot([0, 0.8], [1, 0], color='red', lw=3)        # Diagonal abajo

    # e 
    ax.plot([1.2, 1.8], [0.5, 0.5], color='red', lw=3)  # Linea horizontal
    ax.plot([1.8, 1.2, 1.2, 1.8], [0.5, 1, 0, 0], color='red', lw=3) # Curva

    # v
    ax.plot([2.1, 2.4, 2.7], [1, 0, 1], color='red', lw=3)

    # i 
    ax.plot([3.0, 3.0], [0, 0.8], color='red', lw=3)    # Linea recta
    ax.plot([3.0], [1.1], marker='o', color='red', markersize=5) # Punto

    # n 
    ax.plot([3.3, 3.3], [0, 0.8], color='red', lw=3)    # Linea izq
    ax.plot([3.3, 3.6, 3.9], [0.8, 1, 0.8], color='red', lw=3) # Curva 
    ax.plot([3.9, 3.9], [0.8, 0], color='red', lw=3)    # Linea der
    
    ax.set_title("1. Kevin", loc='left', color='red')

    # 2. NICOLAS
    ax = axes[1]
    # N
    ax.plot([0, 0, 0.8, 0.8], [0, 2, 0, 2], color='blue', lw=3) # Linea iz, diagonal, der
    # i
    ax.plot([1.2, 1.2], [0, 1], color='blue', lw=3) # Linea recta
    ax.plot([1.2], [1.3], marker='o', color='blue', markersize=5) # Punto
    # c 
    ax.plot([2.2, 1.6, 1.6, 2.2], [1, 1, 0, 0], color='blue', lw=3) # Curva
    # o 
    ax.plot([2.5, 3.1, 3.1, 2.5, 2.5], [0, 0, 1, 1, 0], color='blue', lw=3) # Curva
    # l
    ax.plot([3.4, 3.4], [0, 2], color='blue', lw=3) # Linea Recta
    # a
    ax.plot([3.7, 4.3, 4.3, 3.7, 3.7], [0.5, 0.5, 0, 0, 0.5], color='blue', lw=3) # Curva
    ax.plot([4.3, 4.3], [1, 0], color='blue', lw=3) # Linea Recta
    # s 
    ax.plot([5.1, 4.6, 5.1, 4.6], [1, 0.7, 0.3, 0], color='blue', lw=3) 

    ax.set_title("2. Nicolas", loc='left', color='blue')

    # 3. CAMILO
    ax = axes[2]
    # C 
    ax.plot([0.8, 0, 0, 0.8], [2, 2, 0, 0], color='green', lw=3) # Curva
    # a
    ax.plot([1.1, 1.6, 1.6, 1.1, 1.1], [0.5, 0.5, 0, 0, 0.5], color='green', lw=3) # Curva 
    ax.plot([1.6, 1.6], [1, 0], color='green', lw=3) #Linea recta
    # m
    ax.plot([1.9, 1.9], [0, 1], color='green', lw=3) # Linea recta
    ax.plot([1.9, 2.2, 2.5], [1, 1.2, 1], color='green', lw=3) # Curva 1
    ax.plot([2.5, 2.5], [1, 0], color='green', lw=3) # Linea recta
    ax.plot([2.5, 2.8, 3.1], [1, 1.2, 1], color='green', lw=3) # Curva 2
    ax.plot([3.1, 3.1], [1, 0], color='green', lw=3) # Linea recta
    # i
    ax.plot([3.4, 3.4], [0, 1], color='green', lw=3) # Linea recta 
    ax.plot([3.4], [1.3], marker='o', color='green', markersize=5) # Curva
    # l
    ax.plot([3.7, 3.7], [0, 2], color='green', lw=3)
    # o
    ax.plot([4.0, 4.6, 4.6, 4.0, 4.0], [0, 0, 1, 1, 0], color='green', lw=3)

    ax.set_title("3. Camilo", loc='left', color='green')

    # 4. CRISTIAN
    ax = axes[3]
    # C
    ax.plot([0.8, 0, 0, 0.8], [2, 2, 0, 0], color='orange', lw=3)
    # r
    ax.plot([1.1, 1.1], [0, 1], color='orange', lw=3)
    ax.plot([1.1, 1.4, 1.6], [0.6, 1, 0.9], color='orange', lw=3)
    # i
    ax.plot([1.9, 1.9], [0, 1], color='orange', lw=3)
    ax.plot([1.9], [1.3], marker='o', color='orange', markersize=5)
    # s
    ax.plot([2.6, 2.2, 2.6, 2.2], [1, 0.7, 0.3, 0], color='orange', lw=3)
    # t
    ax.plot([2.9, 2.9], [0, 1.6], color='orange', lw=3)
    ax.plot([2.7, 3.1], [1.1, 1.1], color='orange', lw=3) # Cruz de la T
    # i
    ax.plot([3.4, 3.4], [0, 1], color='orange', lw=3)
    ax.plot([3.4], [1.3], marker='o', color='orange', markersize=5)
    # a
    ax.plot([3.7, 4.2, 4.2, 3.7, 3.7], [0.5, 0.5, 0, 0, 0.5], color='orange', lw=3)
    ax.plot([4.2, 4.2], [1, 0], color='orange', lw=3)
    # n
    ax.plot([4.5, 4.5], [0, 1], color='orange', lw=3)
    ax.plot([4.5, 4.8, 5.1], [1, 1.2, 1], color='orange', lw=3)
    ax.plot([5.1, 5.1], [1, 0], color='orange', lw=3)

    ax.set_title("4. Cristian", loc='left', color='orange')

    # 5. ANDRES
    ax = axes[4]
    # A
    ax.plot([0, 0.5, 1.0], [0, 2, 0], color='purple', lw=3)      # Triángulo
    ax.plot([0.25, 0.75], [0.8, 0.8], color='purple', lw=3)     # Barra centro
    # n
    ax.plot([1.3, 1.3], [0, 1], color='purple', lw=3)
    ax.plot([1.3, 1.6, 1.9], [1, 1.2, 1], color='purple', lw=3)
    ax.plot([1.9, 1.9], [1, 0], color='purple', lw=3)
    # d
    ax.plot([2.7, 2.2, 2.2, 2.7, 2.7], [0.5, 0.5, 0, 0, 0.5], color='purple', lw=3) # Curva
    ax.plot([2.7, 2.7], [0, 2], color='purple', lw=3) # Linea recta
    # r
    ax.plot([3.0, 3.0], [0, 1], color='purple', lw=3)
    ax.plot([3.0, 3.3, 3.5], [0.6, 1, 0.9], color='purple', lw=3)
    # e
    ax.plot([3.8, 4.3], [0.5, 0.5], color='purple', lw=3)
    ax.plot([4.3, 3.8, 3.8, 4.3], [0.5, 1, 0, 0], color='purple', lw=3)
    # s
    ax.plot([5.0, 4.6, 5.0, 4.6], [1, 0.7, 0.3, 0], color='purple', lw=3)

    ax.set_title("5. Andres", loc='left', color='purple')

    for ax in axes:
        ax.set_xlim(-0.2, 6.5)
        ax.set_ylim(-0.2, 2.3)
        ax.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    plt.show()

# Resultado
dibujar_nombres()