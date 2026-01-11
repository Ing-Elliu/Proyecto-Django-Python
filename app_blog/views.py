from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor,Libro

def create_autor(request):

    nombre_input = 'Gabriela'
    email_input = 'gabriela@gmail.com'

    autor = Autor.objects.create(name = nombre_input,email = email_input)

    return HttpResponse(f'Se a guardado {nombre_input} con Gmail {email_input}')
