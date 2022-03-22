from django.db import models

# Create your models here.

class Clintes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50,verbose_name='La dirección')
    email=models.EmailField()
    tfno=models.CharField(max_length=7,blank=True,null=True)

    #Para personalizar la muestra de tus clientes y no solo se vea como objetos 
    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()