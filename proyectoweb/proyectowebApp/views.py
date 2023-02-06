from django.shortcuts import render, HttpResponse

# Create your views here.


def presentacion(request):
    return render(request, "proyectowebApp/presentacion.html")

def sitios(request):
    return render(request, "proyectowebApp/sitios.html")

def tienda(request):
    return render(request, "proyectowebApp/tienda.html")

def usuario(request):
    return render(request, "proyectowebApp/usuario.html")

def visitante(request):
    return render(request, "proyectowebApp/visitante.html")