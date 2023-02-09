from django.shortcuts import render, HttpResponse

# Create your views here.


def presentacion(request):
    return render(request, "proyectowebApp/presentacion.html")

def sitios(request):
    return render(request, "proyectowebApp/sitios.html")

def guia(request):
    return render(request, "proyectowebApp/guia.html")

def usuario(request):
    request.post['nombre']
    
    return render(request, "proyectowebApp/usuario.html")

def visitante(request):
    return render(request, "proyectowebApp/visitante.html")