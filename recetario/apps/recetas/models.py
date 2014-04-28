#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User)
    telefono = models.IntegerField()

    def __unicode__(self):
        return "%s - %s" % (self.user, self.telefono,)


class Receta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título', unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField(verbose_name='Preparación', help_text='El proceso de preparación')
    imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, blank=True, null=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')

    def __unicode__(self):
        return self.texto


