import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def pedir_float(mensaje):
    """Pide un número flotante al usuario validando la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")


def clasificar_sistema(zeta):
    """Devuelve el tipo de sistema según el valor de zeta."""
    if zeta == 0:
        return "No amortiguado (oscilación sostenida)"
    elif 0 < zeta < 1:
        return "Subamortiguado"
    elif zeta == 1:
        return "Críticamente amortiguado"
    else:
        return "Sobreamortiguado"


def main():
    print("=== Análisis de sistema de segundo orden ===\n")
    print("La función de transferencia tiene la forma:")
    print("G(s) = (b2*s^2 + b1*s + b0) / (a2*s^2 + a1*s + a0)\n")

    # Coeficientes del numerador 
    print("--- Numerador ---")
    b2 = pedir_float("Ingrese b2 (coef. de s^2): ")
    b1 = pedir_float("Ingrese b1 (coef. de s^1): ")
    b0 = pedir_float("Ingrese b0 (término independiente): ")

    #  Coeficientes del denominador 
    print("\n--- Denominador ---")
    a2 = pedir_float("Ingrese a2 (coef. de s^2): ")
    a1 = pedir_float("Ingrese a1 (coef. de s^1): ")
    a0 = pedir_float("Ingrese a0 (término independiente): ")

    if a2 == 0:
        print("\nError: a2 no puede ser 0 en un sistema de segundo orden.")
        return

    num = [b2, b1, b0]
    den = [a2, a1, a0]

    # Cálculo de wn y zeta a partir de la forma estándar 
    wn = np.sqrt(a0 / a2)
    zeta = a1 / (2 * np.sqrt(a0 * a2))

    tipo_sistema = clasificar_sistema(zeta)

    print("\n=== Resultados ===")
    print(f"Frecuencia natural (wn): {wn:.4f} rad/s")
    print(f"Factor de amortiguamiento (zeta): {zeta:.4f}")
    print(f"Tipo de sistema: {tipo_sistema}")

    # Sistema y respuesta al escalón 
    sistema = signal.TransferFunction(num, den)
    t, y = signal.step(sistema)

    # Gráfica 
    plt.figure(figsize=(8, 5))
    plt.plot(t, y, linewidth=2, color="royalblue")
    plt.title(f"Respuesta al escalón - Sistema {tipo_sistema}\n"
              f"wn = {wn:.3f} rad/s, zeta = {zeta:.3f}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Salida y(t)")
    plt.grid(True)
    plt.axhline(1, color="gray", linestyle="--", linewidth=0.8)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()