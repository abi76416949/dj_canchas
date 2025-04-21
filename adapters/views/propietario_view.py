from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_propietario_view(request):
    return render(request, 'propietario/dashboard.html')
