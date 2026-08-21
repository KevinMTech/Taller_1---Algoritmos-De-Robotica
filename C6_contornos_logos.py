"""
Taller 1 - Punto C.6
Obtenga las coordenadas X y Y de los contornos de dos logos 


"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


logos = {
    "Chevrolet": "chevrolet.png",
    "Mazda": "mazda.png",
}

  
def obtener_contorno(ruta_imagen, umbral=127):
    """
    Carga una imagen, la binariza y devuelve las coordenadas
    (x, y) del contorno más grande encontrado (el logo).
    """

    img = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"No se encontró la imagen: {ruta_imagen}")

    _, binaria = cv2.threshold(img, umbral, 255, cv2.THRESH_BINARY_INV)

    contornos, _ = cv2.findContours(
        binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    contorno_mayor = max(contornos, key=cv2.contourArea)

    x = contorno_mayor[:, 0, 0]
    y = contorno_mayor[:, 0, 1]

    return x, y, img


fig, axes = plt.subplots(1, len(logos), figsize=(10, 5))

for ax, (nombre, ruta) in zip(axes, logos.items()):
    x, y, img_original = obtener_contorno(ruta)

    print(f"Logo: {nombre}")
    print(f"  Número de puntos del contorno: {len(x)}")
    print(f"  Primeras 5 coordenadas (X, Y): {list(zip(x[:5], y[:5]))}")
    print("-" * 50)

    # El eje Y de la imagen crece hacia abajo, se invierte para graficar
    ax.plot(x, -y, linewidth=1.5)
    ax.set_title(f"Contorno: {nombre}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.axis("equal")

plt.tight_layout()
plt.savefig("contornos_logos.png", dpi=150)
plt.show()
