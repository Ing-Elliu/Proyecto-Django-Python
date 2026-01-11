from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Libro(models.Model):
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    cancion = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.cancion