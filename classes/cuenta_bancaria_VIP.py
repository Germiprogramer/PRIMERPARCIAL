from classes.cuenta_bancaria import *

class Cuenta_bancaria_VIP(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo, saldo_negativo):
        super().__init__(ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo)
        self.saldo_negativo = saldo_negativo