from cuenta_bancaria import *

class Cuenta_bancaria_VIP(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo, saldo_negativomax):
        super().__init__(ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo)
        self.saldo_negativomax = saldo_negativomax

    def ingresarVIP(self):
        dinero = int(input("¿¿Cuanta pasta quieres meter?? "))
        self.saldo = self.saldo + dinero
        return self.saldo


    def retirarVIP(self):
        dinero = int(input("¿¿Cuanta pasta quieres sacar?? "))
        if (self.saldo-dinero)>self.saldo_negativomax:
            pass
        else:
            self.saldo = self.saldo - dinero
        return self.saldo

    def transferirVIP(self):
        dinero = int(input("¿¿Cuanta pasta quieres transferir?? "))
        if (self.saldo-dinero)>self.saldo_negativomax:
            pass
        else:
            self.saldo = self.saldo - dinero
            print("Has hecho a alguien más feliz")
        return self.saldo
    
cuenta = Cuenta_bancaria_VIP(1, "si", "ayer", 22, 300, -200)
