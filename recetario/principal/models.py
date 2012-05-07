#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()

	def __unicode__(self):
		return self.nombre

class Receta(models.Model):
	titulo = models.CharField(max_length=100, verbose_name='Título', unique=True)
	ingredientes = models.TextField(help_text='Redacta los ingredientes')
	prepacion = models.TextField(verbose_name='Preparación')
	imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.titulo
