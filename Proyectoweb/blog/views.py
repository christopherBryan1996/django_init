from django.shortcuts import render
from blog.models import Post
# Create your views here.

def blog(req):
    posts=Post.objects.all()
    return render(req,'blog/blog.html',{'posts':posts})

def categorias (req):
    return render(req,'blog/categorias.html')
