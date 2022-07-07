from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=25)
    caracteres = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    genero = models.CharField(max_length=25)
    autor = models.CharField(max_length=25)

