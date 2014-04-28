import json

from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from .models import Receta, Comentario, Perfil
from .forms import RecetaForm, ContactoForm, UsuarioForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from braces.views import LoginRequiredMixin

from django.http import HttpResponse


class AjaxMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class HomeList(ListView):
    context_object_name = 'recetas' # by default is object_list
    model = Receta
    queryset = Receta.objects.order_by('-tiempo_registro')[:10]
    # paginate_by = 5
    template_name = 'recetas/home_list.html'


class UsuarioList(ListView):
    context_object_name = 'usuarios' # by default is object_list
    model = User
    paginate_by = 3
    template_name = 'recetas/usuario_list.html'

    def get_context_data(self, **kwargs):
        context = super(UsuarioList, self).get_context_data(**kwargs)
        recetas = self.get_recetas()
        context.update(dict(recetas=recetas))
        return context

    def get_recetas(self):
        return Receta.objects.all()


class RecetaList(ListView):
    context_object_name = 'recetas' # by default is object_list
    model = Receta
    paginate_by = 3
    queryset = Receta.objects.all()
    template_name = 'recetas/receta_list.html'


class RecetaCreate(LoginRequiredMixin, CreateView):
    form_class = RecetaForm
    model = Receta
    success_url = reverse_lazy('receta_list')
    template_name = 'recetas/receta_form.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        return super(RecetaCreate, self).form_valid(form)


class RecetaDetail(DetailView):
    context_object_name = 'receta' # by default is object_list
    model = Receta

    def get_context_data(self, **kwargs):
        context = super(RecetaDetail, self).get_context_data(**kwargs)
        comentarios = self.get_comentarios()
        context.update(dict(comentarios=comentarios))
        return context

    def get_comentarios(self):
        return Comentario.objects.filter(receta=self.object.pk)


class RecetaUpdate(UpdateView):
    model = Receta
    success_url = reverse_lazy('receta_list')


class RecetaDelete(DeleteView):
    model = Receta
    success_url = reverse_lazy('receta_list')


class ComentarioCreate(CreateView):
    model = Comentario
    success_url = reverse_lazy('receta_list')
    template_name = 'recetas/comentario_form.html'


class AboutTemplate(TemplateView):
    template_name = 'recetas/about.html'


class ContactoFormView(FormView):
    form_class = ContactoForm
    template_name = 'recetas/contacto_form.html'
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        form.send_mail()
        return super(ContactoFormView, self).form_valid(form)


class RegistrarUsuarioFormView(FormView):
    form_class = UsuarioForm
    template_name = "registrar_usuario.html"
    success_url = reverse_lazy('registrar_usuario')

    def form_valid(self, form):
        user = form.save()
        perfil = Perfil()
        perfil.user = user
        perfil.telefono = form.cleaned_data['telefono']
        perfil.save()
        return super(RegistrarUsuarioFormView, self).form_valid(form)
