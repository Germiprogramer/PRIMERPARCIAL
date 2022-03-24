class Libro:
    def __init__(self, nombre, genero, numero_paginas, autor, ISBN):
        self.nombre = nombre
        self.genero = genero
        self.numero_paginas = numero_paginas
        self.autor = autor
        self.ISBN = ISBN

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, a):
        self.nombre = a

    def get_genero(self):
        return self.genero

    def set_genero(self, a):
        self.genero = a

    def get_numero_paginas(self):
        return self.numero_paginas

    def set_numero_paginas(self, a):
        self.numero_paginas = a

    def get_autor(self):
        return self.autor

    def set_autor(self, a):
        self.autor = a

    def get_ISBN(self):
        return self.ISBN

    def set_ISBN(self, a):
        self.ISBN = a

#ejemplo práctico de uso

libro1 = Libro("Harry Potter", "magia", 207, "J.K Rowling", "978-3-16-148410-09-783161-484100")
libro2 = Libro("Diario de Greg", "comedia", 136, "nose", "978-3-16-048410-09-783161-484109")

print("tengo dos libros: {} y {}".format(libro1.get_nombre(), libro2.get_nombre()))

    