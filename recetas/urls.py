from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^sobre/$', views.sobre, name='sobre'),
]