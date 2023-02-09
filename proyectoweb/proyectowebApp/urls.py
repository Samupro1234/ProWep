from django.urls import path
from proyectowebApp import views


urlpatterns = [
    
    path('',views.presentacion, name="Presentacion"),
    path('sitios',views.sitios, name="Sitios"),
    path('guia',views.guia, name="Guia"),
    path('usuario',views.usuario, name="Usuario"),
    path('visitante',views.visitante, name="Visitante"),

]
