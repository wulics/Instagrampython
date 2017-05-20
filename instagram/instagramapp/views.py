from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def home(request):
    return render(request, 'home.html')

def registro(request):
    return render(request, 'registro.html')

def perfil(request):
    return render(request, 'perfil.html')

def crear_usuario(request):
    email = print (request.POST[ 'email' ])
    user = print (request.POST[ 'user' ])
    name = print (request.POST[ 'name' ])
    password = print (request.POST[ 'user' ])
    return render(request, 'registro.html')
