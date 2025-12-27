from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def logout(request, name):
    context = {'name' : name}
    return render(request,'logout.html',context)

def login(request, nombre, cargo):

    tecnologias = ['Python','Django','Flask','PhP','Laravel']
    context = {
        'Nombre' : nombre,
        'Cargo' : cargo,
        'tecnologias' : tecnologias
    }

    return render(request,'login.html',context)

def usuarios(request, nombre, cargo):
    sistemas = ['Kali Linux','Windows Server','Ubuntu serve','MacOs']

    context = {
        'nombre' : nombre,
        'cargo' : cargo,
        'sistemas' : sistemas
    }

    return render(request,'usuario.html',context)