class Cuenta_bancaria:
    def __init__(self, ID, nombre_titular, fecha_de_apertura, numero_cuenta, saldo):
        self.ID = ID
        self.nombre_titular = nombre_titular
        self.fecha_de_apertura = fecha_de_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, a):
        self.saldo = a
    
    def get_numero_cuenta(self):
        return self.numero_cuenta

    def set_numero_cuenta(self, a):
        self.numero_cuenta = a
    
    def get_fecha_de_apertura(self):
        return self.fecha_de_apertura

    def set_fecha_de_apertura(self, a):
        self.fecha_de_apertura = a
    
    def get_nombre_titular(self):
        return self.nombre_titular

    def set_nombre_titular(self, a):
        self.nombre_titular = a

    def get_ID(self):
        return self.ID

    def set_ID(self, a):
        self.ID = a


    def ingresar(self):
        dinero = int(input("¿¿Cuanta pasta quieres meter?? "))
        self.saldo = self.saldo + dinero
        return self.saldo


    def retirar(self):
        dinero = int(input("¿¿Cuanta pasta quieres sacar?? "))
        if dinero>self.saldo:
            pass
        else:
            self.saldo = self.saldo - dinero
        return self.saldo

    def transferir(self):
        dinero = int(input("¿¿Cuanta pasta quieres transferir?? "))
        if dinero>self.saldo:
            pass
        else:
            self.saldo = self.saldo - dinero
            print("Has hecho a alguien más feliz")
        return self.saldo