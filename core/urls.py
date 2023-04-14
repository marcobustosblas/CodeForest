from django.urls import path
from .views import menu, animales, armas, construcciones, consumibles, enemigos, flora, foro, historia, login, logros, lugares, micuenta, recuperar, registro, userform

urlpatterns = [
    path('', menu, name='home'),
    path('Animales.html', animales, name="animales"),
    path('Armas.html', armas, name='armas'),
    path('Construcciones.html', construcciones, name='construcciones'),
    path('Consumibles.html', consumibles, name='consumibles'),
    path('Enemigos.html', enemigos, name='enemigos'),
    path('Flora.html', flora, name='flora'),
    path('forowiki.html', foro, name='foro'),
    path('historia.html', historia, name='historia'),
    path('inicio_sesion_wiki.html', login, name='login'),
    path('Logros.html', logros, name='logros'),
    path('Lugarestf.html', lugares, name='lugares'),
    path('menuprincipal_wiki.html', menu, name="menu"),
    path('micuentatf.html', micuenta, name='micuenta'),
    path('recuperarcontra.html', recuperar, name='recuperar'),
    path('registrase_wiki.html', registro, name='registro'),
    path('userform', userform, name='userform'),
]
