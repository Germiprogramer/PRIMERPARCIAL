from cuenta_bancaria import *

class Cuenta_bancaria_plazofijo(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo):
        super().__init__(ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo)