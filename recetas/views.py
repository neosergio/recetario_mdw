# coding:utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ComentarioForm, ContactoForm, RecetaForm
from .models import Comentario, Receta


@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def comentario_nuevo(request):
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_comentarioform.html', context)

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            try:
                correo.send()
            except Exception as e:
                print('No fue posible enviar el mensaje, revisar la configuración')
                print(e)
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_contactoform.html',context)

def inicio(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas_inicio.html', context)

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(request, 'noactivo.html')
            else:
                return render(request, 'nousuario.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'ingresar.html', context)

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, 'privado.html', context)

def receta(request, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    comentarios = Comentario.objects.filter(receta=dato)
    context = {'receta': dato, 'comentarios': comentarios}
    return render(request, 'recetas_receta.html', context)

def receta_nueva(request):
    if request.method=='POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'recetas_recetaform.html', context)


def recetas(request):
    recetas = Receta.objects.all()
    context = {'datos': recetas}
    return render(request, 'recetas_lista_recetas.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    context = {'recetas': recetas, 'usuarios':usuarios}
    return render(request, 'recetas_usuarios.html', context)

def usuario_nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    context = {'formulario': formulario}
    return render(request, 'nuevousuario.html', context)

def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
