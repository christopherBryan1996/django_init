from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def servicios(req):
    servicios=Servicio.objects.all()
    return render(req,'servicios/servicios.html',{'servicios':servicios})
