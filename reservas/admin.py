from django.contrib import admin
from polideportivos.models import PolideportivoModel
admin.site.register(PolideportivoModel)

from .models import ReservasModel
admin.site.register(ReservasModel)

# Register your models here.
