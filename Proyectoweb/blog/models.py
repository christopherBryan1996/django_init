from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    #modificar los nombres de la base de datos
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    #ponemos el nombre de la carpeta que se va a guardar ya sabe que esta en la posicion de /media
    imagen=models.ImageField(upload_to='blog',null=True, blank=True)
    #hacemos una relacion con los usuarios y con im_delete hacemos que si se borra un usuario se borren todos sus post 
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #una relacios de muchos a muchos
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    #modificar los nombres de la base de datos
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo
