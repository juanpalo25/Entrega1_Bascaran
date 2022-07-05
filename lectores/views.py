from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader

from lectores.models import Blog


def home(request):
    return render(request, 'index.html')

def blogs(request):
    nombre = "Juan"
    primer_vista = loader.get_template('blogs.html')
    primer_blog = Blog(titulo='soy un blog', caracteres = 150 )
    primer_blog.save()
    primer_render = primer_vista.render({'nombre': nombre, 'blog':primer_blog})
    return HttpResponse(primer_render)

def vista_base(request):
    return render(request, 'base.html')