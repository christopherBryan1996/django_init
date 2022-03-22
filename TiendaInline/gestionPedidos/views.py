from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from gestionPedidos.forms import Formulario_contacto

# Create your views here.
def busqueda_productos(req):
    return render(req,'busqueda_productos.html')

def buscar(req):
    if req.GET['prd']:
        #mensaje='Articulo buscado : %r' %req.GET['prd']
        producto=req.GET['prd']
        if len(producto)>20:
            mensaje='texto de busqueda demasiado largo'
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(req,'resultados_busqueda.html',{'articulos':articulos,'query':producto})
    else:
        mensaje='no has intoducido nada'

    return HttpResponse(mensaje)

def contacto(req):
    # de forma manual
    # if req.method=='POST':
    #     subject=req.POST['asunto']
    #     message=req.POST['mensaje']+' '+ req.POST['email']
    #     email_from=settings.EMAIL_HOST_USER
    #     recipient_list=[settings.EMAIL_HOST_USER]
    #     send_mail(subject,message,email_from,recipient_list)
    #     return render(req,"gracias.html")
    # return render(req,'contacto.html')

    if req.method=='POST':
        miFormulario=Formulario_contacto(req.POST)
        if miFormulario.is_valid():
            inf_form= miFormulario.cleaned_data
            send_mail(inf_form['asunto'],inf_form['mensaje'],'mancillabryan1996@outlook.com',[inf_form['email']])
            return render(req,'gracias.html')
    else:
        miFormulario=Formulario_contacto()

    return render(req,'formulario_contacto.html',{'form':miFormulario})
    
