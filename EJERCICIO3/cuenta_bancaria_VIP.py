from cuenta_bancaria import *

class Cuenta_bancaria_VIP(Cuenta_bancaria):
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo, saldo_negativomax):
        super().__init__(ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo)
        self.saldo_negativomax = saldo_negativomax

    def get_saldo_negativomax(self):
        return self.saldo_negativomax

    def set_saldo_negativomax(self, a):
        self.saldo_negativomax = a


    def ingresar(self):
        dinero = int(input("¿¿Cuanta pasta quieres meter?? "))
        self.saldo = self.saldo + dinero
        return self.saldo


    def retirar(self):
        dinero = int(input("¿¿Cuanta pasta quieres sacar?? "))
        if (self.saldo-dinero)>self.saldo_negativomax:
            pass
        else:
            self.saldo = self.saldo - dinero
        return self.saldo

    def transferir(self):
        dinero = int(input("¿¿Cuanta pasta quieres transferir?? "))
        if (self.saldo-dinero)>self.saldo_negativomax:
            pass
        else:
            self.saldo = self.saldo - dinero
            print("Has hecho a alguien más feliz")
        return self.saldo
    
cuenta = Cuenta_bancaria_VIP(1, "si", "ayer", 22, 300, -200)
