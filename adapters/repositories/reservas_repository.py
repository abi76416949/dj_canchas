# adapters/repositories/reserva_repository.py
from reservas.models import ReservasModel

def guardar_reserva(reserva_entidad):
    """
    Guarda una reserva desde la entidad de dominio en la base de datos.
    """
    modelo = ReservasModel.from_entity(reserva_entidad)
    modelo.save()
    return modelo


def obtener_reserva_por_id(reserva_id):
    """
    Obtiene una reserva por su ID.
    """
    return ReservasModel.objects.filter(id=reserva_id).first()


def listar_reservas(limit=10, offset=0):
    """
    Devuelve todas las reservas almacenadas.
    """
    return ReservasModel.objects.all()[offset:offset + limit]



def eliminar_reserva(reserva_id):
    """
    Elimina una reserva por ID.
    """
    return ReservasModel.objects.filter(id=reserva_id).delete()


def actualizar_reserva(reserva_id, datos_actualizados):
    """
    Actualiza los campos de una reserva.
    `datos_actualizados` debe ser un diccionario con los campos a modificar.
    """
    reserva = ReservasModel.objects.filter(id=reserva_id).first()
    if not reserva:
        return None
    # Si la reserva no existe, devolver None
    for campo, valor in datos_actualizados.items():
        setattr(reserva, campo, valor)
    reserva.save()
    # Devolver la reserva actualizada

    return reserva
