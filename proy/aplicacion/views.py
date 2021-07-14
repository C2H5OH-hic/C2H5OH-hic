from django.shortcuts import render
from django.http import HttpResponse


# Aquí es para hacer la llamada hacia una plantilla html
def index(request):
    return render(request, 'aplicacion/inicio.html', {'name': 'Camilo'})

# Aquí es para hacer la llamada desde un texto hecho aquí.
def comoestas(request):
    return HttpResponse('hola oceano')

def bien(request):
    return HttpResponse('hola tierra')
