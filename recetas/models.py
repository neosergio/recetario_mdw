# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Receta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField(verbose_name=u'Preparación', help_text=u'El proceso de preparación')
    imagen = models.ImageField(upload_to='recetas', verbose_name=u'Imágen')
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)

    def __str__(self):
        return self.titulo


@python_2_unicode_compatible
class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text=u'Tú comentario', verbose_name='Comentario')

    def __str__(self):
        return self.texto
