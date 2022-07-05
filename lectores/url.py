from .views import home, blogs, vista_base
from django.urls import path

urlpatterns = [
    path('', home),
    path('blogs/', blogs),
    path('base/', vista_base)
]