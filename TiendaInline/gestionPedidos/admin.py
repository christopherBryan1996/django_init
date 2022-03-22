from re import search
from django.contrib import admin
from gestionPedidos.models import Clintes,Articulos,Pedidos

class Clientes_admin(admin.ModelAdmin):
    #nos sirve para mostrar las columnas deseadas
    list_display=('nombre','direccion', 'tfno')
    #nos sirve para busqueda, de ciertas columnas
    search_fields=('nombre','tfno')

class Articulos_admin(admin.ModelAdmin):
    #nos crea todo un filto de la columna espesifias
    list_filter=('seccion',)

class Pedidos_admin(admin.ModelAdmin):
    list_display=('numero','fecha')
    list_filter=('fecha',)
    date_hierarchy='fecha'

# Register your models here.
admin.site.register(Clintes, Clientes_admin)
admin.site.register(Articulos, Articulos_admin)
admin.site.register(Pedidos, Pedidos_admin)