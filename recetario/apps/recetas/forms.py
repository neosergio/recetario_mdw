#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Receta, Comentario

from django.contrib.auth.forms import UserCreationForm


class ContactoForm(forms.Form):
    correo = forms.EmailField(label="Tu correo electrónico")
    mensaje = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        titulo = 'Mensaje desde el recetario'
        contenido = ''


class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = ('titulo','ingredientes','preparacion','imagen',)


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario


class UsuarioForm(UserCreationForm):
    telefono = forms.IntegerField()