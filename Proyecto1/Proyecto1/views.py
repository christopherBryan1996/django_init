from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

#definimos el objeto persona
class Persona(object):
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):#primera vista 
    #creamos un objeto
    p1=Persona('Bryan','Mancilla')
    nombre='Juan'
    apellido='Díaz'
    ahora= datetime.now()
    #cargar una plantilla de forma manual 
    doc_externo=open('C:/Users/manci/Documents/django_init/Proyecto1/Proyecto1/platillas/saludos.html')
    plt= Template(doc_externo.read())
    doc_externo.close()
    #si no se tiene que pasar argumentos se deja basia
    #ctx=Context()
    ctx=Context({'nombre_persona':nombre,'apellido_persona':apellido,'momento_actual':ahora,'creador':p1})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(req):
    return HttpResponse('adios')

def dameFecha(req):

    fecha_actual=datetime.now()
    documento="""
        <html>
            <body>
                <h1>%s</h1>
            </body>
        </html>
    """ % fecha_actual
    return HttpResponse(documento)

def calculaEdad(req,edad,year):
    edadActual=edad
    periodo= year-2022
    edadFutura = edadActual+periodo
    documento= """
        <html>
            <body>
                <h2>En el año %s tendras %s años</h2>
            </body>
        </html>
    """ % (year,edadFutura)
    return HttpResponse(documento)