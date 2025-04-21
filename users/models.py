from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

TIPO_USUARIO_CHOICES = [
    ('admin', 'Administrador'),
    ('cliente', 'Cliente'),
    ('propietario', 'Propietario'),
]

class User(AbstractUser):
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')

    # 👇 Aquí agregamos los related_name para evitar conflictos con auth.User
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Permisos específicos asignados a este usuario.'
    )

    def es_cliente(self):
        return self.tipo_usuario == 'cliente'

    def es_propietario(self):
        return self.tipo_usuario == 'propietario'

    def es_admin(self):
        return self.tipo_usuario == 'admin'

# usuarios/models.py

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    # otros campos...
class Propietario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    # otros campos...
