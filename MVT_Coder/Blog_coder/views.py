from django.shortcuts import render
from Blog_coder.models import Familiares
from django.template import loader
from django.http import HttpResponse



# Create your views here.

def Listado_Familiares(request):
    
    lista_de_Familiares = Familiares.objects.all()
    
        
    familia = { "lista_familiares": lista_de_Familiares}

    plantilla = loader.get_template("Blog_coder/index.html")

    documento = plantilla.render(familia)
    #return render(request, "Blog_coder/index.html")

    return HttpResponse(documento)