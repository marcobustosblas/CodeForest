from django.shortcuts import render, redirect
from .models import USER
from .forms import UserForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def animales(request):
    return render(request, 'core/Animales.html')

def armas(request):
    return render(request, 'core/Armas.html')

def construcciones(request):
    return render(request, 'core/Construcciones.html')

def consumibles(request):
    return render(request, 'core/Consumibles.html')

def enemigos(request):
    return render(request, 'core/Enemigos.html')

def flora(request):
    return render(request, 'core/Flora.html')

def foro(request):
    return render(request, 'core/forowiki.html')

def historia(request):
    return render(request, 'core/historia.html')

def login(request):
    return render(request, 'core/inicio_sesion_wiki.html') #OJO!!!!

def logros(request):
    return render(request, 'core/Logros.html')

def lugares(request):
    return render(request, 'core/Lugarestf.html')

def menu(request):
    return render(request, 'core/menuprincipal_wiki.html')

def micuenta(request):
    return render(request, 'core/micuentatf.html')

def recuperar(request):
    return render(request, 'core/recuperarcontra.html')

def registro(request):
    return render(request, 'core/registrase_wiki.html')

def userform(request):
    datos = {
        'form':UserForm()
    }
    if request.method == 'POST':
        formulario = UserForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Usuario Registrado')
            return redirect('registro')
        else:
            messages.error(request, 'No se puedo registrar')
            return redirect('registro')
    
    return render(request, 'core/registrase_wiki.html', datos)
