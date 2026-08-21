
"Punto 5A: Realice en funciones las rotaciones X,Y y Z, donde se tenga un parametro"
"de entrada (angulo) y un parametro de salida (matriz)"

import numpy 

def rotacion_x(angulo_grados):
   
    rad = numpy.radians(angulo_grados)
    cos, sen = numpy.cos(rad), numpy.sin(rad)
    
    matriz_rx = numpy.array([
        [1,  0,  0],
        [0,  cos, -sen],
        [0,  sen,  cos]
    ])
    return numpy.round(matriz_rx, 4)


def rotacion_y(angulo_grados):

    rad = numpy.radians(angulo_grados)
    cos, sen = numpy.cos(rad), numpy.sin(rad)
    
    matriz_ry = numpy.array([
        [ cos,  0,  sen],
        [ 0,  1,  0],
        [-sen,  0,  cos]
    ])
    return numpy.round (matriz_ry, 4)


def rotacion_z(angulo_grados):
  
    rad = numpy.radians(angulo_grados)
    cos, sen = numpy.cos(rad), numpy.sin(rad)
    
    matriz_rz = numpy.array([
        [cos, -sen,  0],
        [sen,  cos,  0],
        [0,  0,  1]
    ])
    return numpy.round(matriz_rz, 4)

# Asignacion de angulo
angulo = 90

m_rx = rotacion_x(angulo)
m_ry = rotacion_y(angulo)
m_rz = rotacion_z(angulo)

# Aplicar la matriz a un punto en 3D mediante producto matricial (@)
punto_origen = numpy.array([1.0, 0.0, 0.0])
punto_rotado = m_rz @ punto_origen

# Imprimir resultado
print("- Matriz Rotación X -")
print(m_rx)

print("\n- Matriz Rotación Y -")
print(m_ry)

print("\n- Matriz Rotación Z -")
print(m_rz)
