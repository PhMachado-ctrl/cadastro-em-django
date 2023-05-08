from django.shortcuts import render

def home(request):
    #Retorna o Arquivo home.html
    return render(request,'usuarios/home.html')

def usuarios(request):
    pass