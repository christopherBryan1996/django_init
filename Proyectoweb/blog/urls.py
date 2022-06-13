import imp
from django.urls import path
from blog.views import blog,categorias

urlpatterns = [
    path('',blog,name='Blog'),
    path('categoria',categorias,)
]