# domain/reservas.py

from datetime import date, time

class Reserva:
    def __init__(self, nombre: str, telefono: str, email: str, cancha_id: int, fecha: date,
                 hora_inicio: time, hora_fin: time, id: int = None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.cancha_id = cancha_id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"Reserva({self.nombre}, {self.fecha}, {self.hora_inicio}-{self.hora_fin})"
