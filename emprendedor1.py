# utilidades = p*u-gt

# P = Precio Suscripcion
# U = Numero de usuarios
# GT = Gastos totales

precio = input('Ingrese el precio de suscripcion: ')
precio = float(precio)

usuarios = input('Ingrese numero de usuarios:' )
usuarios = float(usuarios)

gastoTotal = input('Ingrese gasto total:')
gastoTotal = float(gastoTotal)

utilidades = precio*usuarios-gastoTotal

print('Su Utilidad es de:', utilidades )
