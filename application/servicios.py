# application/servicios.py
from domain.polideportivos import Polideportivo
from domain.courts import Court
from domain.reservas import Reserva
def crear_polideportivo(nombre, ubicacion, contacto):
    # Aquí podrías agregar lógica de negocio extra o validaciones
    nuevo = Polideportivo(nombre, ubicacion, contacto)
    # Normalmente se llamaría al repositorio para persistirlo
    return nuevo

def crear_court(nombre, descripcion, precio_dia, precio_noche, tipo, polideportivo_id):
    return Court(nombre, descripcion, precio_dia, precio_noche, tipo, polideportivo_id)


def crear_reserva(nombre, telefono, email, cancha_id, fecha, hora_inicio, hora_fin):
    # Aquí podrías agregar validaciones, verificar disponibilidad, etc.
    return Reserva(
        nombre=nombre,
        telefono=telefono,
        email=email,
        cancha_id=cancha_id,
        fecha=fecha,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin
    )

