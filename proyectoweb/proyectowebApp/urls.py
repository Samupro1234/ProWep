from django.urls import path
from proyectowebApp import views


urlpatterns = [
    path('',views.presentacion, name="Presentacion"),
    path('sitios',views.sitios, name="Sitios"),
    path('tienda',views.tienda, name="tienda"),
    path('blog',views.blog, name="blog"),
    path('contactos',views.contactos, name="contactos"),

]
