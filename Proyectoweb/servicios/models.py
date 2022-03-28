from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    #ponemos el nombre de la carpeta que se va a guardar ya sabe que esta en la posicion de /media
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    #modificar los nombres de la base de datos
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo