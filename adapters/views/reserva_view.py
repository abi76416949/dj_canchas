from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from reservas.models import ReservasModel
from courts.models import CourtModel
from datetime import date, timedelta
from application.servicios import crear_reserva

# Crear reserva
class CrearReservaView(View):
    def get(self, request):
        canchas = CourtModel.objects.all()
        return render(request, 'reservas/crear_reserva.html', {'canchas': canchas})

    def post(self, request):


        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        cancha_id = int(request.POST.get('cancha_id'))
        fecha = request.POST.get('fecha')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')

        reserva_entidad = crear_reserva(nombre, telefono, email, cancha_id, fecha, hora_inicio, hora_fin)
        reserva_model = ReservasModel(
            nombre=reserva_entidad.nombre,
            telefono=reserva_entidad.telefono,
            email=reserva_entidad.email,
            cancha_id=reserva_entidad.cancha_id,
            fecha=reserva_entidad.fecha,
            hora_inicio=reserva_entidad.hora_inicio,
            hora_fin=reserva_entidad.hora_fin,
        )
        reserva_model.save()
        return redirect('reserva_exitosa')


# Listar reservas
class ListaReservasView(View):
    def get(self, request, polideportivo_id, court_id):
        # Aquí obtenemos las reservas relacionadas con la cancha (court)
        reservas = ReservasModel.objects.filter(cancha_id=court_id)  # Asegúrate de usar el campo correcto para las relaciones

        # Puedes pasar los datos de reservas a la plantilla
        return render(request, 'listar_reservas.html', {'reservas': reservas})

# Editar reserva
class EditarReservaView(View):
    def get(self, request, pk):
        reserva = get_object_or_404(ReservasModel, pk=pk)
        canchas = CourtModel.objects.all()
        return render(request, 'reservas/editar_reserva.html', {'reserva': reserva, 'canchas': canchas})

    def post(self, request, pk):
        reserva = get_object_or_404(ReservasModel, pk=pk)
        reserva.nombre = request.POST.get('nombre')
        reserva.telefono = request.POST.get('telefono')
        reserva.email = request.POST.get('email')
        reserva.cancha_id = int(request.POST.get('cancha_id'))
        reserva.fecha = request.POST.get('fecha')
        reserva.hora_inicio = request.POST.get('hora_inicio')
        reserva.hora_fin = request.POST.get('hora_fin')
        reserva.save()
        return redirect('lista_reservas')


# Eliminar reserva
class EliminarReservaView(View):
    def post(self, request, pk):
        reserva = get_object_or_404(ReservasModel, pk=pk)
        reserva.delete()
        return redirect('lista_reservas')

