from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def genshin_impact(request):

    personajes = ['Hutao','Raiden Shogun','Keching','Citlali'] 
    context = {
               'personajes' : personajes
               }
    
    return render(request,'genshin.html',context)

def hokai_star_rail(request):

    personajes = ['Evernigth','Sparkle','Cyrene','Robin']
    context = {
        'personajes' : personajes
    }

    return render(request,'hokai_star_rail.html',context)

def wutering_waves(request):

    personajes = ['Carlotta','Lupa','Phrolova','Iuno']
    context = {
        'personajes' : personajes
    }

    return render(request,'wutering_waves.html',context)