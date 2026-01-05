from django.db import models

class Personaje(models.Model):

    Nombre = models.CharField(max_length=30)
    Genero = models.TextField()
    Edad = models.IntegerField()
    Universo = models.TextField()

    def __str__(self):
        return self.Nombre

# Create your models here.
