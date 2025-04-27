
# canchas/urls.py
from django.contrib import admin
from django.urls import path
from adapters.views.polideportivo_view import crear_polideportivo_view, listar_polideportivos_view
from django.conf import settings
from django.conf.urls.static import static

from adapters.views import polideportivo_view, court_view, reserva_view, auth_view
from adapters.views.court_view import crear_court_view, listar_court_view
from adapters.views.auth_view import redireccionar_usuario, login_view, logout_view
from django.contrib.auth import views as auth_views
from adapters.views.propietario_view import dashboard_propietario_view
from adapters.views                                    .cliente_view import dashboard_cliente_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear/', crear_polideportivo_view, name="crear_polideportivo"),
    
    path('crear_court/', crear_court_view, name="crear_court"),
    

   

    path('', polideportivo_view.listar_polideportivos_view, name='listar_polideportivos'),

    # Ruta para listar canchas  de un polideportivo
    path('polideportivo/<int:polideportivo_id>/courts/', court_view.listar_court_view, name='listar_courts'),

    # LISTAR RESERVAS  DE UNA CAHCHA
    path(
        'polideportivo/<int:polideportivo_id>/courts/<int:court_id>/reservas/',
        reserva_view.ListaReservasView.as_view(),
        name='listar_reservas'
    ),


   # Ruta para crear una reserva
    path(
        'polideportivo/<int:polideportivo_id>/cancha/<int:court_id>/reservar/',
        reserva_view.CrearReservaView.as_view(),
        name='crear_reserva'
        ),
    
    path('redireccionar/', redireccionar_usuario, name='redireccionar_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('propietario/dashboard/', dashboard_propietario_view, name='dashboard_propietario'),
    path('cliente/dashboard/', dashboard_cliente_view, name='dashboard_cliente'),

 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
