def mostrar_interes(cuenta):
    """
    Función que recibe un objeto Cuenta
    y ejecuta el método calcular_interes
    """
    print(f"Titular: {cuenta.get_titular()}")
    print(f"Interés generado: ${cuenta.calcular_interes():.2f}")
