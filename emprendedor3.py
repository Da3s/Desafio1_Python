# utilidades = (p*u-gt)-ua

# P = Precio Suscripcion
# U = Numero de usuarios
# GT = Gastos totales
# UA = Utilidad anterior

precio = int(input('Ingrese el precio de suscripcion: '))

usuarios = int(input('Ingrese numero de usuarios: '))

gastoTotal = int(input('Ingrese gasto total: '))

utilidades = (precio*usuarios-gastoTotal)

utilidadAnterior = int(input('Ingrese Utilidad anterior: '))

if utilidadAnterior > 0:
    
    utilidad_actual_anterior = utilidades / utilidadAnterior
    print('La razon de su utilidad actual versus la anterior es de:', round(utilidades,2))
else:
      print("Las utilidades no pueden ser iguales a cero")



