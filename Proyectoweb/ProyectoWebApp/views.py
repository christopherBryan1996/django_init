from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'ProyectoWebApp/home.html')

def servicios(req):
    return render(req,'ProyectoWebApp/servicios.html')

def tienda(req):
    return render(req,'ProyectoWebApp/tienda.html')
def blog(req):
    return render(req,'ProyectoWebApp/blog.html')

def contacto(req):
    return render(req,'ProyectoWebApp/contacto.html')