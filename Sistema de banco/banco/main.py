from servicios.operaciones import mostrar_interes
from modelo.cuenta import CuentaAhorros, CuentaCorriente

# Crear objetos
cuenta1 = CuentaAhorros("María", 1500)
cuenta2 = CuentaCorriente("Luis", 2000)

# Mostrar resultados de gestion
mostrar_interes(cuenta1)
mostrar_interes(cuenta2)

