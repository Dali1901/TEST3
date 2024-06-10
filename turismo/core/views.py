from django.shortcuts import render
from .models import Informe
# Create your views here.
def principal(request):
    return render(request, "core/principal.html")

def destinos(request):
    return render(request, "core/destinos.html")

def practicas(request):
    return render(request, "core/practicas.html")

def guias(request):
    return render(request, "core/guias.html")

def conoce(request):
    return render(request, "core/conoce.html")

def aprende(request):
    informes = Informe.objects.all()
    return render(request, "core/aprende.html", {'informes':informes})
