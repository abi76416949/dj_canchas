# adapters/views/auth_view.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def redireccionar_usuario(request):
    user = request.user
    if hasattr(user, 'es_admin') and user.es_admin():
        return redirect('admin:index')
    elif hasattr(user, 'es_propietario') and user.es_propietario():
        return redirect('dashboard_propietario')
    elif hasattr(user, 'es_cliente') and user.es_cliente():
        return redirect('dashboard_cliente')
    else:
        return redirect('login')

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('redireccionar_usuario')
        else:
            context['error'] = 'Usuario o contraseña incorrectos'
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
