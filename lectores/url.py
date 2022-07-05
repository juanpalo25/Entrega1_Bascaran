from .views import home, blogs, vista_base
from django.urls import path

urlpatterns = [
    path('', home, name= 'home'),
    path('blogs/', blogs, name='blogs'),
    path('base/', vista_base)
]