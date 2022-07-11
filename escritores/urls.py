from . import views 
from django.urls import path


urlpatterns = [
    path('crear_resenia/',views.ListadoResenias.as_view() , name='crear_resenia'),
    path('listado_resenias/',views.CrearResenia.as_view() , name='listado_resenias'),
    path('editar_resenia/<int:id>',views.EditarResenia.as_view() , name='editar_resenia'),
    path('eliminar_resenia/<int:id>',views.EliminarResenia.as_view() ,  name='eliminar_resenia'),
    path('mostar_resenia/<int:id>',views.MostrarResenia.as_view() ,  name='mostrar_resenia'),

]
