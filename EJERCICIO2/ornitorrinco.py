from animal import * 
from animal_mamifero import *

class Ornitorrinco(Animal_mamifero):
    def __init__(self, nombre, tamaño):
        super().__init__(nombre, tamaño)
    
    def hacer_sonidoraro():
        print("grrrrrr")