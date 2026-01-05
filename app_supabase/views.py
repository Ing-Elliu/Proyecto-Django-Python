from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def tester(request):
    return HttpResponse('Hola desde una app de Django')

#formas de guardar y borrar datos de manera directa, ejemplo 2, delete correcto
def create(request):
    persona = Comment(name = 'Cyndi Luper', score = 90)
    persona.save()

    return HttpResponse(f"Se guardo {persona.name}, en la fecha {persona.date}")

def delete(request):
    persona = Comment.objects.get(id = 4)
    nombre = persona.name
    persona.delete()

    return HttpResponse(f"Se a borrado {nombre} ")