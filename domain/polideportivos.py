class Polideportivo:
    def __init__(self, nombre, ubicacion, contacto):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.contacto = contacto


    def __str__(self):
        return f"{self.nombre} ({self.ubicacion})"