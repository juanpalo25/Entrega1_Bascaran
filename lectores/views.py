from django.http import HttpResponse
from django.template import Context, Template, loader


def home(request):
    primer_vista = loader.get_template('base.html')
    nombre = 'Juan'
    primer_render = primer_vista.render({'nombre': nombre})
    return HttpResponse(primer_render)
