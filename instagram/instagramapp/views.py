from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def home(request):
    return render(request, 'home.html')

def registro(request):
    return render(request, 'registro.html')
