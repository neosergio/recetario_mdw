from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Comentario, Receta


def inicio(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas_inicio.html', context)

def receta(request, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    comentarios = Comentario.objects.filter(receta=dato)
    context = {'receta': dato, 'comentarios': comentarios}
    return render(request, 'recetas_receta.html', context)

def recetas(request):
    recetas = Receta.objects.all()
    context = {'datos': recetas}
    return render(request, 'recetas_lista_recetas.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    context = {'recetas': recetas, 'usuarios':usuarios}
    return render(request, 'recetas_usuarios.html', context)

def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
