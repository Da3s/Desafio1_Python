# utilidades = (p*u-gt)-ua

# P = Precio Suscripcion
# U = Numero de usuarios
# GT = Gastos totales
# UA = Utilidad anterior

precio = float(input('Ingrese el precio de suscripcion: '))

usuarios = float(input('Ingrese numero de usuarios: '))

gastoTotal = float(input('Ingrese gasto total: '))

utilidadAnterior = float(input('Ingrese Utilidad anterior: '))

utilidades = (precio*usuarios-gastoTotal)

print('La razon de su utilidad actual versus la anterior es de:', round(utilidades,2))
utilidad_actual_anterior = utilidades / utilidadAnterior

