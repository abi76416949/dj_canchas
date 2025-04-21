# reservas/models.py
from django.db import models
from courts.models import CourtModel  # Importa desde la app correcta

class ReservasModel(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    cancha = models.ForeignKey(CourtModel, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora_inicio}"

    @classmethod
    def from_entity(cls, reserva_entidad):
        return cls(
            nombre=reserva_entidad.nombre,
            telefono=reserva_entidad.telefono,
            email=reserva_entidad.email,
            court_id=reserva_entidad.court_id,
            fecha=reserva_entidad.fecha,
            hora_inicio=reserva_entidad.hora_inicio,
            hora_fin=reserva_entidad.hora_fin
        )
