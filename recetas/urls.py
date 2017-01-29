from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^recetas/$', views.recetas, name='lista_recetas'),
    url(r'^receta/(?P<id_receta>\d+)$', views.receta, name='detalle_receta'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^sobre/$', views.sobre, name='sobre'),
]