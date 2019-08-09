from django.urls import reverse_lazy

from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)

from .models import Actividades, Canales, Clientes
from .forms import ClienteFormulario, ClienteFiltro

class Listado(ListView, FormView):
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            if form.cleaned_data['nombre']:
                self.object_list = self.object_list.filter(nombre__icontains=form.cleaned_data['nombre'])
            if form.cleaned_data['actividad']:
                self.object_list = self.object_list.filter(actividad=form.cleaned_data['actividad'])
            if form.cleaned_data['estadocliente']:
                self.object_list = self.object_list.filter(estadocliente=form.cleaned_data['estadocliente'])
            if form.cleaned_data['califica']:
                self.object_list = self.object_list.filter(califica=form.cleaned_data['califica'])

        return self.render_to_response(self.get_context_data(object_list=self.object_list.order_by('fantasia'), form=form))

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('fantasia')

    model = Clientes
    form_class = ClienteFiltro
    template_name = 'clientes/listado.html'
    success_url = reverse_lazy('clientes:show')
    paginate_by = 25


class Detalle(DetailView):
    model = Clientes
    template_name = 'clientes/detalle.html'


class Crear(CreateView):
    model = Clientes
    form_class = ClienteFormulario
    success_url = reverse_lazy('clientes:show')
    template_name = 'clientes/crear.html'


class Editar(UpdateView):
    model = Clientes
    form_class = ClienteFormulario
    success_url = reverse_lazy('clientes:show')
    template_name = 'clientes/actualizar.html'


class Eliminar(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes:show')
    template_name = 'clientes/eliminar.html'


class Actividad_Listado(ListView):
    def get_queryset(self):
        return Canales.objects.order_by('descripcion')

    model = Canales
    template_name = 'actividades/listado.html'


class Actividad_Filtro(ListView):
    def get_queryset(self):
        return Canales.objects.order_by('descripcion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['actividades'] = Actividades.objects.filter(idcanales=self.kwargs['pk']).order_by('descripcion')
        return context

    template_name = 'actividades/listado.html'
