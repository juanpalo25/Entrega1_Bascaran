from django.http import HttpResponse
from django.template import Context, Template, loader

from lectores.models import Blog


def home(request):
    primer_vista = loader.get_template('base.html')
    nombre = 'Juan'
    primer_blog = Blog(titulo='soy un blog', caracteres = 150 )
    primer_blog.save()
    primer_render = primer_vista.render({'nombre': nombre, 'blog':primer_blog})
    return HttpResponse(primer_render)
