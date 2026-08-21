import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Constantes de la norma IEC 60751 para PT100
# ----------------------------------------------------------------------
R0 = 100.0          # Resistencia nominal a 0 °C (ohm)
A = 3.9083e-3        # Coeficiente A (1/°C)
B = -5.775e-7        # Coeficiente B (1/°C^2)
C = -4.183e-12       # Coeficiente C (1/°C^4), válido solo para T < 0 °C

# ----------------------------------------------------------------------
# Parámetros configurables (edítalos aquí, sin necesidad de consola)
# ----------------------------------------------------------------------
TEMPERATURAS_PUNTUALES = [-50, 0, 25, 100, 200, 500]  # °C, valores a evaluar
T_MIN, T_MAX = -200, 850                              # Rango de la curva


def resistencia_pt100(T, R0=R0, A=A, B=B, C=C):

    T = np.asarray(T, dtype=float)

    # Ecuación válida para T >= 0
    R_pos = R0 * (1 + A * T + B * T**2)

    # Ecuación válida para T < 0
    R_neg = R0 * (1 + A * T + B * T**2 + C * (T - 100) * T**3)

    # Selección condicional según el signo de la temperatura
    R = np.where(T >= 0, R_pos, R_neg)

    # Si la entrada era un escalar, devolver un escalar
    if R.ndim == 0:
        return float(R)
    return R


def main():

    print("Resultados puntuales:")
    print("-" * 30)
    print(f"{'T (°C)':>10} | {'R (ohm)':>10}")
    print("-" * 30)
    for T_val in TEMPERATURAS_PUNTUALES:
        R_val = resistencia_pt100(T_val)
        print(f"{T_val:10.1f} | {R_val:10.4f}")
    print("-" * 30)


    T = np.linspace(T_MIN, T_MAX, 1000)
    R = resistencia_pt100(T)


    T_tabla = np.arange(T_MIN, T_MAX + 1, 50)
    R_tabla = resistencia_pt100(T_tabla)

    print("\nTabla de referencia (T vs R):")
    print("-" * 30)
    print(f"{'T (°C)':>10} | {'R (ohm)':>10}")
    print("-" * 30)
    for t, r in zip(T_tabla, R_tabla):
        print(f"{t:10.1f} | {r:10.4f}")
    print("-" * 30)

    plt.figure(figsize=(8, 5))
    plt.plot(T, R, color="tab:blue", linewidth=2, label="R(T) - PT100")
    plt.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.axhline(100, color="gray", linestyle="--", linewidth=0.8)
    plt.scatter([0], [100], color="red", zorder=5, label="R0 = 100 Ω @ 0 °C")

    # Marcar las temperaturas puntuales definidas por el usuario
    R_puntual = resistencia_pt100(TEMPERATURAS_PUNTUALES)
    plt.scatter(TEMPERATURAS_PUNTUALES, R_puntual, color="orange",
                zorder=5, label="Valores puntuales")

    plt.title("Resistencia de una RTD PT100 en función de la temperatura")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Resistencia (Ω)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Guarda la gráfica como imagen (útil si se ejecuta sin entorno gráfico)
    plt.savefig("curva_PT100.png", dpi=150)
    print("\nGráfica guardada como 'curva_PT100.png'")

    plt.show()


if __name__ == "__main__":
    main()