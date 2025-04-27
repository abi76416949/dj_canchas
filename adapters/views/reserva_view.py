from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from reservas.models import ReservasModel
from courts.models   import CourtModel
from application.servicios import crear_reserva
from datetime import datetime

# Crear reserva (y mostrar calendario)
class CrearReservaView(View):
    def get(self, request, polideportivo_id, court_id):
        court = get_object_or_404(CourtModel, id=court_id)
        reservas = ReservasModel.objects.filter(cancha_id=court_id)

        return render(request, 'reservas/crear_reserva.html', {
            'court': court,
            'reservas': reservas,
            'court_id': court_id,
        })

    def post(self, request, polideportivo_id, court_id):
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        fecha = request.POST['fecha']
        hora_inicio = request.POST['hora_inicio']
        hora_fin = request.POST['hora_fin']

        ReservasModel.objects.create(
            nombre=nombre,
            telefono=telefono,
            email=email,
            cancha_id=court_id,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
        )
        return redirect('reserva_exitosa')


# Listar reservas de una cancha
class ListaReservasView(View):
    def get(self, request, polideportivo_id, court_id):
        reservas = ReservasModel.objects.filter(cancha_id=court_id)
        return render(request, 'listar_reservas.html', {
            'reservas': reservas,
            'polideportivo_id': polideportivo_id,
            'court_id': court_id,
        })
    
    def post(self, request, polideportivo_id, court_id):
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        fecha_raw = request.POST['fecha']

        # Convertir correctamente la fecha
        fecha = datetime.fromisoformat(fecha_raw).date()  
        # fromisoformat() acepta strings tipo '2025-04-27T08:30:00-05:00'
        # .date() extrae solo el día

        hora_inicio = request.POST['hora_inicio']
        hora_fin = request.POST['hora_fin']

        ReservasModel.objects.create(
            nombre=nombre,
            telefono=telefono,
            email=email,
            cancha_id=court_id,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin
        )

        reservas = ReservasModel.objects.filter(cancha_id=court_id)
        return render(request, 'listar_reservas.html', {
            'reservas': reservas,
            'polideportivo_id': polideportivo_id,
            'court_id': court_id,
            'mensaje': '¡Reserva realizada con éxito!'
        })

# Editar una reserva existente
class EditarReservaView(View):
    def get(self, request, pk):
        reserva = get_object_or_404(ReservasModel, pk=pk)
        courts = CourtModel.objects.all()
        return render(request, 'reservas/editar_reserva.html', {
            'reserva': reserva,
            'courts': courts,
        })

    def post(self, request, pk):
        reserva = get_object_or_404(ReservasModel, pk=pk)
        reserva.nombre = request.POST['nombre']
        reserva.telefono = request.POST['telefono']
        reserva.email = request.POST['email']
        reserva.cancha_id = int(request.POST['cancha_id'])
        reserva.fecha = request.POST['fecha']
        reserva.hora_inicio = request.POST['hora_inicio']
        reserva.hora_fin = request.POST['hora_fin']
        reserva.save()

        # Para redirigir, si no tienes polideportivo en el modelo, puedes obtenerlo a través de la cancha:
        polideportivo_id = reserva.cancha.polideportivo.id  # O si ya lo tienes en la URL, úsalo directamente.
        return redirect('listar_reservas', polideportivo_id=polideportivo_id, court_id=reserva.cancha_id)


# Eliminar reserva
class EliminarReservaView(View):
    def post(self, request, pk):
        reserva = get_object_or_404(ReservasModel, pk=pk)
        # Usamos la relación para obtener el polideportivo:
        polideportivo_id = reserva.cancha.polideportivo.id
        c_id = reserva.cancha_id
        reserva.delete()
        return redirect('listar_reservas', polideportivo_id=polideportivo_id, court_id=c_id)
