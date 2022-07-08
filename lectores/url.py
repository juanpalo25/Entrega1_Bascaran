from .views import home, crear_blog, vista_base, listado_blogs, editar_blog, eliminar_blog
from django.urls import path


urlpatterns = [
    path('', home, name= 'home'),
    path('crear_blog/', crear_blog, name='crear_blog'),
    path('base/', vista_base),
    path('listado_blogs/', listado_blogs, name='listado_blogs'),
    path('editar_blog/<int:id>', editar_blog, name='editar_blog'),
    path('eliminar_blog/<int:id>', eliminar_blog, name='eliminar_blog'),
]

