#importacion libreria

import math

# Declaracion de variables

radio = input('Ingrese radio(km)):')
radio = float(radio)

constante = input('Ingrese la constante g(m/s2):')
constante = float(constante)

radio = radio * 1000


resultado = (math.sqrt(2*radio*constante))

print('La velocidad de escape es ', round(resultado,1))

