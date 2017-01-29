from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),
    url(r'^comenta/$', views.comentario_nuevo, name='comentario_nuevo'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^privado', views.privado, name='privado'),
    url(r'^recetas/$', views.recetas, name='lista_recetas'),
    url(r'^receta/nueva/$', views.receta_nueva, name='receta_nueva'),
    url(r'^receta/(?P<id_receta>\d+)$', views.receta, name='detalle_receta'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuario/nuevo/$', views.usuario_nuevo, name='usuario_nuevo'),
    url(r'^sobre/$', views.sobre, name='sobre'),
]