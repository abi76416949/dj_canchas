# domain/courts.py

class Court:
    def __init__(self, nombre, descripcion, precio_dia, precio_noche, tipo, polideportivo_id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_dia = precio_dia
        self.precio_noche = precio_noche
        self.tipo = tipo
        self.polideportivo_id = polideportivo_id
        
