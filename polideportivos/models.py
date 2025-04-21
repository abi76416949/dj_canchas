from django.db import models
from users.models import Propietario
class PolideportivoModel(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='polideportivos/', blank=True, null=True)  
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='polideportivos')


    def __str__(self):
        return self.nombre

    @classmethod
    def from_entity(cls, polideportivo):
        return cls(
            nombre=polideportivo.nombre,
            ubicacion=polideportivo.ubicacion,
            contacto=polideportivo.contacto,
            imagen=polideportivo.imagen
        )

# Create your models here.
