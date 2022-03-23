from django.urls import path
from ProyectoWebApp.views import home,servicios,tienda,blog,contacto

urlpatterns = [
    path('',home,name='Home'),
    path('servicios/',servicios,name='Sercicios'),
    path('tienda/',tienda,name='Tienda'),
    path('blog/',blog,name='Blog'),
    path('contacto/',contacto,name='Contacto'),
]