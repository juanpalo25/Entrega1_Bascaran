from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader
from .models import Blog


def home(request):
    return render(request, 'index.html')

def blogs(request):
    template = loader.get_template('blogs.html')
    b1 = Blog(titulo='soy el 1er blog', caracteres = 12)
    b2 = Blog(titulo='soy el 2do blog', caracteres = 45)
    b3 = Blog(titulo='soy el 3er blog', caracteres = 23)
    render = template.render({'lista_objetos': [b1,b2,b3]})
    return HttpResponse(render)

def vista_base(request):
    return render(request, 'base.html')