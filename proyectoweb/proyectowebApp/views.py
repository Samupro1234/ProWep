from django.shortcuts import render, HttpResponse
from proyectowebAppAforo.models import usuario, guia, sitio, visitante
# Create your views here.


def presentacion(request):
    return render(request, "proyectowebApp/presentacion.html")

def usuario(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        usuario = usuario(nombre=nombre, apellido=apellido, email=email, password=password)
        usuario.save()
        return render(request, "proyectowebApp/usuario.html")
        print('hola')
    return render(request, "proyectowebApp/usuario.html")

def sitios(request):
    if request.method == "POST":
        nombre_sitio = request.POST['sitio']
        aforo = request.POST['aforo']
        sitios = sitio(nombre_sitio=nombre_sitio, aforo=aforo)
        sitios.save()
        return render(request, "proyectowebApp/sitios.html")
    return render(request, "proyectowebApp/sitios.html")

def guia(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        guia = guia(nombre=nombre, apellido=apellido, email=email, password=password)
        guia.save()
        print("vjdsnvjdnvjdsamu")
        return render(request, "proyectowebApp/guia.html")
    

    return render(request, "proyectowebApp/guia.html")


def visitante(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        visitante = visitante(nombre=nombre, apellido=apellido, email=email, password=password)
        visitante.save()
        return render(request, "proyectowebApp/visitante.html")
    return render(request, "proyectowebApp/visitante.html")