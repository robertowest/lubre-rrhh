from django.urls import reverse_lazy

from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)

from .models import Clientes
from .forms import ClienteFormulario, ClienteFiltro
import pdb

class Listado(ListView, FormView):
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            if form.cleaned_data['nombre']:
                self.object_list = self.object_list.filter(nombre__icontains=form.cleaned_data['nombre']) | \
                                   self.object_list.filter(fantasia__icontains=form.cleaned_data['nombre'])
            if form.cleaned_data['actividad']:
                self.object_list = self.object_list.filter(actividad=form.cleaned_data['actividad'])
            if form.cleaned_data['estadocliente']:
                self.object_list = self.object_list.filter(estadocliente=form.cleaned_data['estadocliente'])
            if form.cleaned_data['califica']:
                self.object_list = self.object_list.filter(califica=form.cleaned_data['califica'])

        # pdb.set_trace()
        return self.render_to_response(self.get_context_data(object_list=self.object_list.order_by('fantasia'), form=form))

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('fantasia')

    model = Clientes
    form_class = ClienteFiltro
    template_name = 'listado.html'
    success_url = reverse_lazy('clientes:show')
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
