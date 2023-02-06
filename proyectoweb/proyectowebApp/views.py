from django.shortcuts import render, HttpResponse

# Create your views here.


def presentacion(request):
    return render(request, "proyectowebApp/presentacion.html")

def sitios(request):
    return render(request, "proyectowebApp/sitios.html")

def tienda(request):
    return render(request, "proyectowebApp/tienda.html")

def blog(request):
    return render(request, "proyectowebApp/blog.html")

def contactos(request):
    return render(request, "proyectowebApp/contactos.html")