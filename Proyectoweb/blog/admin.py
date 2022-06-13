from django.contrib import admin
from .models import Categoria,Post

class CategoriaAdmi(admin.ModelAdmin):
    readonly_fields=('created','update')

class PostAdmi(admin.ModelAdmin):
    readonly_fields=('created','update')

# Register your models here.
admin.site.register(Categoria,CategoriaAdmi)
admin.site.register(Post,PostAdmi)