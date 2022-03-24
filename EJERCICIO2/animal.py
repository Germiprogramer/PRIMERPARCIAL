class Animal:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, a):
        self.nombre = a