from django.shortcuts import render

# Create your views here.

def Listado_Familiares(request):
    return render(request, "Blog_coder/index.html")