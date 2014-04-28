from django.conf.urls import patterns, include, url
from .views import (HomeList,
                    RecetaList,
                    UsuarioList,
                    RecetaCreate,
                    ComentarioCreate,
                    RecetaUpdate,
                    RecetaDetail,
                    RecetaDelete,
                    AboutTemplate,
                    ContactoFormView,
                    RegistrarUsuarioFormView
                )


urlpatterns = patterns('',

    url(r'^$', HomeList.as_view(), name='home_list'),
    url(r'^recetas/$', RecetaList.as_view(), name='receta_list'),
    url(r'^usuarios/$', UsuarioList.as_view(), name='usuario_list'),
    url(r'^about/$', AboutTemplate.as_view(), name='receta_about'),
    url(r'^contacto/$', ContactoFormView.as_view(), name='contacto_form'),
    url(r'^registrar/$', RegistrarUsuarioFormView.as_view(), name='registrar_usuario'),

    url(r'^receta/(?P<pk>\d+)$', RecetaDetail.as_view(), name='receta_detail'),

    # url(r'^edit/(?P<pk>\d+)$', RecetaUpdate.as_view(), name='receta_edit'),
    url(r'^receta/nueva$', RecetaCreate.as_view(), name='receta_create'),
    url(r'^comenta/$', ComentarioCreate.as_view(), name='comentario_create'),

    # url(r'^delete(?P<pk>\d+)$', RecetaDelete.as_view(), name='receta_delete'),
)
