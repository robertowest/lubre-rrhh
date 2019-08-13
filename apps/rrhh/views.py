from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from .models import Empleado
from .forms import EmpleadoPersonaModelForm

def home(request):
    return render(request, 'rrhh_home.html')


class EmpleadoShow(ListView):
    model = Empleado
    template_name = 'empleado/listado.html'
    paginate_by = 25


class EmpleadoDetail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = context['empleado'].comunicaciones.all()
        return context

    model = Empleado
    # form_class = Empleado
    template_name = 'empleado/detalle.html'


# class EmpleadoUpdate(MultiModelForm):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['persona'] = context['empleado'].persona .comunicaciones.all()
#         return context
#
#     model = Empleado
#     form_class = EmpleadoFormulario
#     success_url = reverse_lazy('empleado:empl_show')
#     template_name = 'empleado/detalle.html'

class EmpleadoCreate(CreateView):
    # def form_valid(self, form):
    #     persona = form['persona'].save()
    #     empleado = form['empleado'].save(commit=False)
    #     empleado.persona = persona
    #     empleado.save()
    #     return reverse_lazy('clientes:show')

    form_class = EmpleadoPersonaModelForm
    template_name = 'empleado/detalle.html'
    success_url = reverse_lazy('clientes:show')


class EmpleadoUpdate(UpdateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={'persona': self.object.persona, 'empleado': self.object})
        return kwargs

    # def form_valid(self, form):
    #     persona = form['persona'].save()
    #     empleado = form['empleado'].save(commit=False)
    #     empleado.persona = persona
    #     empleado.save()
    #     return reverse_lazy('clientes:show')

    model = Empleado
    form_class = EmpleadoPersonaModelForm
    template_name = 'empleado/detalle.html'
