from django.shortcuts import render
from .models import BlogNoticia, CarruselPrincipal
# Create your views here.

def inicio(request):
    carrusel = CarruselPrincipal.objects.all()
    return render(request, 'index.html', {
        'carrusel':carrusel
    })

def aboutUs(request):
    return render(request, 'about.html')