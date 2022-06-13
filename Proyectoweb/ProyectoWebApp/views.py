from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req,'ProyectoWebApp/home.html')

def tienda(req):
    return render(req,'ProyectoWebApp/tienda.html')


def contacto(req):
    return render(req,'ProyectoWebApp/contacto.html')