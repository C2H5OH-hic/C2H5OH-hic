from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def holaa(request):
    return render(request, 'holaa.html', {'name': 'Camilo'})

def comoestas(request):
    return HttpResponse('hola oceano')

def bien(request):
    return HttpResponse('hola tierra')
