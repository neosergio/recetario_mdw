from django.contrib import admin
from .models import Receta, Comentario, Perfil


admin.site.register(Perfil)
admin.site.register(Receta)
admin.site.register(Comentario)
