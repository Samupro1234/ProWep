from django.shortcuts import render, HttpResponse
from proyectowebAppAforo.models import usuario
# Create your views here.


def presentacion(request):
    return render(request, "proyectowebApp/presentacion.html")

def sitios(request):
    return render(request, "proyectowebApp/sitios.html")

def guia(request):
    return render(request, "proyectowebApp/guia.html")

def usuario(request):
    #user = usuarioss.objects.all()
        
    #request.post['nombre']
    
    return render(request, "proyectowebApp/usuario.html")

def visitante(request):
    return render(request, "proyectowebApp/visitante.html")