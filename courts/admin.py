from django.contrib import admin
from django import forms
from .models import CourtModel, TIPO_OPCIONES
from django.contrib.postgres.forms import SimpleArrayField

class CourtAdminForm(forms.ModelForm):
    tipo = forms.MultipleChoiceField(
        choices=TIPO_OPCIONES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = CourtModel
        fields = '__all__'

class CourtAdmin(admin.ModelAdmin):
    form = CourtAdminForm

admin.site.register(CourtModel, CourtAdmin)
