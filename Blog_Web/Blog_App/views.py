from django.shortcuts import render, HttpResponse

# Create your views here.

def base(request):
    return render(request, "Blog_App/base.html")

def inicio(request):
    return render(request, "Blog_App/inicio.html")

def mundo(request):
    return render(request, "Blog_App/mundo.html")

def gastronomía(request):
    return render(request, "Blog_App/gastronomía.html")

def recetas(request):
    return render(request, "Blog_App/Recetas.html")

def mensajes(request):
    return render(request, "Blog_App/mensajes.html") 