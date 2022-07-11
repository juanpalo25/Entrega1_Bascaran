from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=25)
    caracteres = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    genero = models.CharField(max_length=25)
    autor = models.CharField(max_length=25)
    def __str__(self):
        return f'TITULO: {self.titulo}'

class Reseña(models.Model):
    pelicula = models.CharField(max_length=25)
    sinopsis = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    genero = models.CharField(max_length=25)
    director = models.CharField(max_length=25)
    def __str__(self):
        return f'PELICULA: {self.pelicula}'