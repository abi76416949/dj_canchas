# adapters/views/court_view.py

from django.shortcuts import render, redirect
from application.servicios import crear_court
from adapters.repositories.court_repository import guardar_court
from courts.models import CourtModel

def crear_court_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio_dia = float(request.POST.get("precio_dia"))
        precio_noche = float(request.POST.get("precio_noche"))
        tipo = request.POST.getlist("tipo")  # campo múltiple (checklist o select multiple)
        polideportivo_id = int(request.POST.get("polideportivo_id"))

        cancha = crear_court(nombre, descripcion, precio_dia, precio_noche, tipo, polideportivo_id)
        guardar_court(cancha)
        return redirect("crear_court")

    return render(request, "crear_court.html")


def listar_court_view(request):
    courts = CourtModel.objects.all()
    return render(request, "listar_court.html", {"courts": courts})


def editar_court_view(request, pk):
    court = CourtModel.objects.get(pk=pk)
    if request.method == "POST":
        court.nombre = request.POST.get("nombre")
        court.descripcion = request.POST.get("descripcion")
        court.precio_dia = float(request.POST.get("precio_dia"))
        court.precio_noche = float(request.POST.get("precio_noche"))
        court.tipo = request.POST.getlist("tipo")
        court.polideportivo_id = int(request.POST.get("polideportivo_id"))
        court.save()
        return redirect("listar_court")
    return render(request, "editar_court.html", {"court": court})
