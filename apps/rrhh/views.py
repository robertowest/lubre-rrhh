from betterforms.multiform import MultiModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Empleado, Comunicacion
from .forms import EmpleadoMultiForm, ComunicacionForm


def home(request):
    return render(request, 'rrhh_home.html')


class EmpleadoShow(ListView):
    model = Empleado
    template_name = 'empleado/listado.html'
    paginate_by = 25


class EmpleadoDetail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comunicaciones'] = context['empleado'].comunicaciones.all()
        context['comunicaciones'] = Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id)
        return context

    model = Empleado
    # form_class = Empleado
    template_name = 'empleado/detalle.html'


class EmpleadoCreate(CreateView):
    form_class = EmpleadoMultiForm
    template_name = 'empleado/formulario.html'
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoUpdate(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={'persona': self.object.persona, 'empleado': self.object})
        return kwargs

    model = Empleado
    form_class = EmpleadoMultiForm
    template_name = 'empleado/formulario.html'
    success_url = reverse_lazy('rrhh:empl_show')

    # def get_success_url(self):
    #     return reverse_lazy('rrhh:empl_detail', kwargs={'pk': self.object.pk})
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comunicaciones'] = context['empleado'].comunicaciones.all()
    #     return context
    #
    # def form_valid(self, form):
    #     persona = form['persona'].save()
    #     empleado = form['empleado'].save(commit=False)
    #     empleado.persona = persona
    #     empleado.save()
    #     return reverse_lazy('rrhh:empl_show')


class EmpleadoUpdate(DeleteView):
    pass


class CanalCreate(CreateView):
    form_class = ComunicacionForm
    template_name = 'comunicacion/formulario.html'
