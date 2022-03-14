from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

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
    # doc_externo=open('C:/Users/manci/Documents/django_init/Proyecto1/Proyecto1/platillas/saludos.html')
    # plt= Template(doc_externo.read())
    # doc_externo.close()
    #si no se tiene que pasar argumentos se deja basia
    #ctx=Context()
    # ctx=Context({'nombre_persona':nombre,'apellido_persona':apellido,'momento_actual':ahora,'creador':p1,"temas":["Plantillas",'Modelos','Formularios','Vistas','Despliegue']})
    # documento=plt.render(ctx)

    #cargar pantilla buenas practicas 
    #doc_externo= loader.get_template('saludos.html')
    #documento=doc_externo.render({'nombre_persona':nombre,'apellido_persona':apellido,'momento_actual':ahora,'creador':p1,"temas":["Plantillas",'Modelos','Formularios','Vistas','Despliegue']})
    #return HttpResponse(documento)
    return render(request,'saludos.html',{'nombre_persona':nombre,'apellido_persona':apellido,'momento_actual':ahora,'creador':p1,"temas":["Plantillas",'Modelos','Formularios','Vistas','Despliegue']})

def curso_c(req):
    fecha_actual=datetime.now()

    return render(req,'CursoC.html',{'dameFecha':fecha_actual})

def curso_css(req):
    fecha_actual=datetime.now()

    return render(req,'cursoCss.html',{'dameFecha':fecha_actual})

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