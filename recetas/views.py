# coding:utf-8

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactoForm, RecetaForm
from .models import Comentario, Receta


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
    #return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))
    return render(request, 'recetas_contactoform.html',context)

def inicio(request):
    recetas = Receta.objects.all()
    context = {'recetas': recetas}
    return render(request, 'recetas_inicio.html', context)

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

def sobre(request):
    html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
    return HttpResponse(html)
