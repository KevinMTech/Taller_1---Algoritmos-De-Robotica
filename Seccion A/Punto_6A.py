
"Punto 6A: Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumatico doble efecto."
"Debe establecer previamente los valores de presion, asi como las dimensiones fisicas del cilindro para realizar el calculo"

import math

def fuerza_cilindro():
    
    presion_bar = 6.0          # Presion en bar
    diametro_piston_mm = 80.0  # Diametro del piston en mm
    diametro_vstg_mm = 20.0    # Diametro del vastago en mm

    # Presion: 1 bar = 100,000 Pa (N/m²)
    presion_pa = presion_bar * 100000
    
    # Diametro a metro
    d_piston_m = diametro_piston_mm / 1000
    d_vstg_m = diametro_vstg_mm / 1000

    # Area de avance 
    area_avance = (math.pi / 4) * (d_piston_m ** 2)
    
    # Area de retroceso
    area_retroceso = (math.pi / 4.0) * ((d_piston_m ** 2) - (d_vstg_m ** 2))

    # Fuerza = Presion * Area
    fuerza_avance = presion_pa * area_avance
    fuerza_retroceso = presion_pa * area_retroceso 
    
    return {
        "presion_bar": presion_bar,
        "fuerza_avance_N": round(fuerza_avance, 2),
        "fuerza_retroceso_N": round(fuerza_retroceso, 2)
    }

resultados = fuerza_cilindro()

fuerza_avance = resultados["fuerza_avance_N"]
fuerza_retroceso = resultados["fuerza_retroceso_N"]

print(f"Fuerza de avance: {fuerza_avance} N")
print(f"Fuerza de retroceso: {fuerza_retroceso} N")