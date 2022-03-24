from EJERCICIO2.animal import *

class Animal_mamifero(Animal):
    def __init__(self, nombre, tamaño):
        super().__init__(nombre, tamaño)
    
    def parir(self):
        print("nuestro pequeño {} ha parido un hijo".format(self.nombre))