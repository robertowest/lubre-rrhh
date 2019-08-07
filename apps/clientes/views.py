from django import forms
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)

from .models import Clientes
from .forms import ClienteFormulario

class Listado(ListView):
    model = Clientes
    template_name = 'listado.html'
    paginate_by = 25


class Detalle(DetailView):
    model = Clientes
    template_name = 'detalle.html'


class Crear(CreateView):
    model = Clientes
    form_class = ClienteFormulario
    success_url = reverse_lazy('clientes:show')
    template_name = 'crear.html'


class Editar(UpdateView):
    model = Clientes
    form_class = ClienteFormulario
    success_url = reverse_lazy('clientes:show')
    template_name = 'actualizar.html'


class Eliminar(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes:show')
    template_name = 'eliminar.html'

