# adapters/repositories/polideportivo_repository.py
from polideportivos.models import PolideportivoModel

def guardar_polideportivo(polideportivo):
    modelo = PolideportivoModel.from_entity(polideportivo)
    modelo.save()
    return modelo
