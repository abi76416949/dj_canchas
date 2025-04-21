# adapters/repositories/court_repository.py

from courts.models import CourtModel

def guardar_court(court):
    return CourtModel.objects.create(
        nombre=court.nombre,
        descripcion=court.descripcion,
        precio_dia=court.precio_dia,
        precio_noche=court.precio_noche,
        tipo=court.tipo,
        polideportivo_id=court.polideportivo_id
    )