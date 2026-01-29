# Clase base
class Cuenta:
    def __init__(self, titular, saldo):
        # Encapsulación: atributos privados
        self.__titular = titular
        self.__saldo = saldo

    def calcular_interes(self):
        """
        Método polimórfico que será sobrescrito
        por las clases hijas
        """
        return 0

    # Métodos getter
    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo


# Clase derivada: Cuenta de Ahorros
class CuentaAhorros(Cuenta):
    def calcular_interes(self):
        # Polimorfismo: interés fijo
        return self.get_saldo() * 0.03


# Clase derivada: Cuenta Corriente
class CuentaCorriente(Cuenta):
    def calcular_interes(self):
        # Polimorfismo: interés menor
        return self.get_saldo() * 0.01

