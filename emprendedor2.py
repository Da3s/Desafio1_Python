# utilidades = (p*un)+((p*1.5)*up)-gt

# P = Precio Suscripcion
# U = Numero de usuarios
# UP = Usuarios Premium
# GT = Gastos totales


precio = float(input('Ingrese el precio de suscripcion: '))

usuariosNormal = float(input('Ingrese numero de usuarios normales:' ))
usuariosPremium = float(input('Ingrese numero de usuarios premium:' ))

gastoTotal = float(input('Ingrese gasto total:'))

utilidades = (precio*usuariosNormal)+((precio*1.5)*usuariosPremium)-gastoTotal

print('Su Utilidad es de:', utilidades )