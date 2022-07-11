
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.base import View
from .models import Resenia

class ListadoResenias(ListView):
    model= Resenia
    template_name= 'resenia/listado_resenias.html'

class CrearResenia():
    model= Resenia
    template_name= 'resenia/crear_resenia.html'


class EditarResenia():
    model= Resenia
    template_name= 'resenia/editar_resenia.html'


class EliminarResenia():
    model= Resenia
    template_name= 'resenia/eliminar_resenia.html'

class MostrarResenia():
    ...
