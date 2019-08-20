from betterforms.multiform import MultiModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView

from .models import Empleado, Comunicacion, Denuncia_ART, Domicilio
from .forms import EmpleadoMultiForm, ComunicacionForm, EmpleadoFiltro


def home(request):
    return render(request, 'rrhh_home.html')


class EmpleadoShow(ListView, FormView):
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            if form.cleaned_data['nombre']:
                self.object_list = self.object_list.filter(persona__nombre__icontains=form.cleaned_data['nombre'])
            if form.cleaned_data['apellido']:
                self.object_list = self.object_list.filter(persona__apellido__icontains=form.cleaned_data['apellido'])
            if form.cleaned_data['active']:
                self.object_list = self.object_list.filter(active=form.cleaned_data['active'])
        return self.render_to_response(self.get_context_data(object_list=self.object_list.order_by('persona'), form=form))

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('persona')

    model = Empleado
    form_class = EmpleadoFiltro
    template_name = 'empleado/listado.html'
    paginate_by = 25
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoDetail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comunicaciones'] = context['empleado'].comunicaciones.all()
        context['domicilio'] = \
            Domicilio.objects.filter(empleado_id=context['empleado'].persona_id)
        context['comunicaciones'] = \
            Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id).order_by('tipo')
        context['denuncias'] = Denuncia_ART.objects.filter(empleado_id=context['empleado'].persona_id)
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
        context['comunicaciones'] = \
            Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id).order_by('tipo')
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


class EmpleadoDelete(DeleteView):
    pass


class CanalCreate(CreateView):
    form_class = ComunicacionForm
    template_name = 'comunicacion/formulario.html'
