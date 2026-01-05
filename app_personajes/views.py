from django.shortcuts import render
from django.http import HttpResponse
from .models import Personaje

def personajes(request):
    return HttpResponse('Hola desde la galeria de personajes')

def create (request):
    #personaje = Personaje(Nombre = 'Raiden',Genero = 'Fantasia,suspenso',Edad = 23,Universo ='Genshin Impact')
    #personaje.save()

    personaje = Personaje.objects.create(Nombre = 'Furina',Genero = 'Fantasia,suspenso',Edad = 18,Universo ='Genshin Impact')

    return HttpResponse('Prueba de ORM')

def delete(request):

    #personaje = Personaje.objects.get(id = 1)
    #personaje.delete()

    Personaje.objects.filter(id=2).delete()
    return HttpResponse('Ruta para borrar personajes')
