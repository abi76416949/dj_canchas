from django.contrib.auth import get_user_model
from users.models import Propietario, Cliente  # Ajusta a tu ruta real
from polideportivos.models import PolideportivoModel
from courts.models import CourtModel

User = get_user_model()

def run():
    # Primero los usuarios
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword',
            tipo_usuario='admin'
        )
        print("✅ Usuario Admin creado.")

    if not User.objects.filter(username='propietario1').exists():
        propietario_user = User.objects.create_user(
            username='propietario1',
            email='propietario@example.com',
            password='propietariopassword',
            tipo_usuario='propietario'
        )
        Propietario.objects.create(
            user=propietario_user,
            documento='12345678',
            nombre='Propietario Nombre',
            apellido='Propietario Apellido',
            telefono='999999999'
        )
        print("✅ Propietario creado.")

    if not User.objects.filter(username='cliente1').exists():
        cliente_user = User.objects.create_user(
            username='cliente1',
            email='cliente@example.com',
            password='clientepassword',
            tipo_usuario='cliente'
        )
        Cliente.objects.create(
            user=cliente_user,
            telefono='888888888'
        )
        print("✅ Cliente creado.")

    # Opcional: Crear polideportivo y cancha para que no esté vacío
    if not PolideportivoModel.objects.exists():
        poli = PolideportivoModel.objects.create(
            nombre='Polideportivo Demo',
            ubicacion='Calle Falsa 123'
        )
        CourtModel.objects.create(
            nombre='Cancha 1',
            descripcion='Una cancha demo',
            precio_dia=50,
            precio_noche=80,
            polideportivo=poli,
            tipo=["césped", "sin techo"]
        )
        print("✅ Polideportivo y cancha creados.")
