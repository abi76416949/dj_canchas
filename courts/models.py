from django.db import models
from polideportivos.models import PolideportivoModel
from django.contrib.postgres.fields import ArrayField  # para usar arrays

TIPO_OPCIONES = [
    ("con techo", "Con techo"),
    ("sin techo", "Sin techo"),
    ("iluminación", "Iluminación LED"),
    ("césped", "Césped sintético"),
    ("graderías", "Con graderías"),
]
class CourtModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_dia = models.FloatField()
    precio_noche = models.FloatField()
    #aqui hacemos la relación
    polideportivo = models.ForeignKey(PolideportivoModel, on_delete=models.CASCADE, related_name='courts')
    imagen = models.ImageField(upload_to='courts/', blank=True, null=True)  

    # Requiere PostgreSQL

    tipo = ArrayField(
        base_field=models.CharField(max_length=50),
        default=list,
        blank=True
    )
    def __str__(self):
        return self.nombre


