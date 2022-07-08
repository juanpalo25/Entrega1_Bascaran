from django import forms

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    caracteres = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    genero = forms.CharField(max_length=25)
    autor = forms.CharField(max_length=25)

class Busqueda_blog(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)