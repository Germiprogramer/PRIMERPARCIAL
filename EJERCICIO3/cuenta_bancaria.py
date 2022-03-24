class Cuenta_bancaria:
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo):
        self.ID = ID
        self.nombre_titular = nombre_titular
        self.fecha_de_apertura = fecha_de_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def ingresar(self):
        dinero = int(input("¿¿Cuanta pasta quieres meter?? "))
        self.saldo = self.saldo + dinero
        return self.saldo


    def retirar(self):
        dinero = int(input("¿¿Cuanta pasta quieres sacar?? "))
        self.saldo = self.saldo - dinero
        return self.saldo

    def transferir(self):
        dinero = int(input("¿¿Cuanta pasta quieres transferir?? "))
        self.saldo = self.saldo - dinero
        print("Has hecho a alguien más feliz")
        return self.saldo