#importacion libreria

import math

# Declaracion de variables

radio = float(input('Ingrese radio(km)):'))
print(type(radio)) 

constante = float(input('Ingrese la constante g(m/s2):'))
print(type(constante)) 

constante = constante * 1000


resultado = (math.sqrt(2*radio*constante))



print(type(resultado)) 

print('La velocidad de escape es ', round(resultado,1))

