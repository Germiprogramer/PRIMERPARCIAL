from cuenta_bancaria import *

class Cuenta_bancaria_plazofijo(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo, fecha_de_vencimiento):
        super().__init__(ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo)
        self.fecha_de_vencimiento = fecha_de_vencimiento

    def get_fecha_de_vencimiento(self):
        return self.fecha_de_vencimiento

    def set_fecha_de_vencimiento(self, a):
        self.fecha_de_vencimiento= a

    
    def retirar(self):
        dinero = int(input("¿¿Cuanta pasta quieres sacar?? "))
        fecha = input("Es antes de la fecha de vencimiento??  si / no")

        if fecha == "si":
            dinero = dinero + dinero * 0.05
        else:
            pass

        if dinero>self.saldo:
            pass
        else:
            self.saldo = self.saldo - dinero
        return self.saldo