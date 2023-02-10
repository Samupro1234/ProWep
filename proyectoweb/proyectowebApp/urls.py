from django.urls import path
from proyectowebApp import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.presentacion, name="Presentacion"),
    path('sitios',views.sitios, name="Sitios"),
    path('guia',views.guia, name="Guia"),
    path('usuario',views.usuario, name="Usuario"),
    path('visitante',views.visitante, name="Visitante"),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)