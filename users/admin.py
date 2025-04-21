from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Propietario, Cliente

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'tipo_usuario', 'is_staff', 'is_active')
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Rol en el sistema', {'fields': ('tipo_usuario',)}),

    )
@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'telefono', 'user')
    search_fields = ('nombre', 'apellido', 'documento')
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono')
