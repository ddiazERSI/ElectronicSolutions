from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, "webpage/inicio.html")

def nosotros(request):
    return render(request, "webpage/nosotros.html")
    
def servicios(request):
    return render(request, "webpage/servicios.html")
    
def portafolio(request):
    return render(request, "webpage/portafolio.html")

def contacto(request):
    return render(request, "webpage/contacto.html")
    