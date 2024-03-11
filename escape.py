#importacion libreria

import math

# Declaracion de variables

radio = float(input('Ingrese radio(km)):'))

constante = float(input('Ingrese la constante g(m/s2):'))

constante = constante * 1000


resultado = (math.sqrt(2*radio*constante))

print('La velocidad de escape es ', round(resultado,1))

