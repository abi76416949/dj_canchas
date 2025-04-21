# adapters/views/polideportivo_view.py
from django.shortcuts import render, redirect
from application.servicios import crear_polideportivo
from adapters.repositories.polideportivo_repository import guardar_polideportivo

def crear_polideportivo_view(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        ubicacion = request.POST.get("ubicacion")
        contacto = request.POST.get("contacto")
        # Llamamos al caso de uso
        polideportivo = crear_polideportivo(nombre, ubicacion, contacto)
        guardar_polideportivo(polideportivo)
        return redirect("listar_polideportivos")
    return render(request, "crear_polideportivo.html")

 
def listar_polideportivos_view(request):
    from polideportivos.models import PolideportivoModel
    polideportivos = PolideportivoModel.objects.all()
    return render(request, "listar_polideportivos.html", {"polideportivos": polideportivos})
