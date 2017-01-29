from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .models import Receta


def inicio(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas_inicio.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    context = {'recetas': recetas, 'usuarios':usuarios}
    return render(request, 'recetas_usuarios.html', context)

def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
