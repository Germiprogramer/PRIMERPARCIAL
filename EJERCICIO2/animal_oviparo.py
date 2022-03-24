from animal import *

class Animal_oviparo(Animal):
    def __init__(self, nombre, tamaño):
        super().__init__(nombre, tamaño)
    
    def poner_huevo(self):
        print("nuestro pequeño {} ha puesto un huevo".format(self.nombre))