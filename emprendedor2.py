# utilidades = (p*un)+((p*1.5)*up)-gt

# P = Precio Suscripcion
# U = Numero de usuarios
# UP = Usuarios Premium
# GT = Gastos totales


precio = input('Ingrese el precio de suscripcion: ')
precio = float(precio)

usuariosNormal = input('Ingrese numero de usuarios normales:' )
usuariosNormal = float(usuariosNormal)
usuariosPremium = input('Ingrese numero de usuarios premium:' )
usuariosPremium = float(usuariosPremium)

gastoTotal = input('Ingrese gasto total:')
gastoTotal = float(gastoTotal)

utilidades = (precio*usuariosNormal)+((precio*1.5)*usuariosPremium)-gastoTotal

print('Su Utilidad es de:', utilidades )