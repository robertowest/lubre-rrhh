from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django.urls import reverse_lazy

from apps.rrhh import models, forms


def index(request):
    empl_id = 0
    if not request.user.is_anonymous:
        usuario = request.user
        try:
            empleado = models.Empleado.objects.get(user_id=usuario.id)
            empl_id = empleado.persona.id
        except:
            empl_id = 0
    return render(request, 'empleado/index.html', {'empl_id': empl_id})


class EmpleadoShow(LoginRequiredMixin, ListView, FormView):
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
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(active=form.fields['active'].initial)

        return queryset.order_by('persona')

    model = models.Empleado
    form_class = forms.EmpleadoFiltro
    template_name = 'empleado/listado.html'
    paginate_by = 25
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoDetail(LoginRequiredMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comunicaciones'] = context['empleado'].comunicaciones.all()
        context['domicilio'] = \
            models.Domicilio.objects.filter(empleado_id=context['empleado'].persona_id)
        context['comunicaciones'] = \
            models.Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id).order_by('tipo')
        context['denuncias'] = models.Denuncia_ART.objects.filter(empleado_id=context['empleado'].persona_id)
        context['activos'] = models.ActivoMantenimientoView.objects.filter(responsable_id=context['empleado'].persona_id)
        return context

    model = models.Empleado
    # form_class = Empleado
    template_name = 'empleado/detalle.html'
    # template_name = 'empleado/activos.html'


class EmpleadoCreate(LoginRequiredMixin, CreateView):
    login_url = '/usuarios/inicio/'
    form_class = forms.EmpleadoMultiForm
    template_name = 'empleado/formulario.html'
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunicaciones'] = \
            models.Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id).order_by('tipo')
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(instance={'persona': self.object.persona, 'empleado': self.object})
        return kwargs

    model = models.Empleado
    form_class = forms.EmpleadoMultiForm
    template_name = 'empleado/formulario.html'
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    pass


class CanalCreate(LoginRequiredMixin, CreateView):
    form_class = forms.ComunicacionForm
    template_name = 'comunicacion/formulario.html'


class VacacionesReadView(LoginRequiredMixin, ListView):
    template_name = 'empleado/vacaciones/index.html'
    # model = models.Vacaciones
    # context_object_name = 'data'
    #context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(VacacionesReadView, self).get_context_data(**kwargs)
        context['empl_id'] = self.kwargs['empl_id']
        context['empleado'] = models.Empleado.objects.get(persona_id=self.kwargs['empl_id'])
        return context

    def get_queryset(self):
        empl_id = self.kwargs['empl_id']
        filtro = Q(empleado_id=empl_id) & Q(active=True)

        # queryset = {'empleado': models.Empleado.objects.get(id=empl_id),
        #             'vacaciones': models.Vacaciones.objects.filter(filtro)}
        queryset = models.Vacaciones.objects.filter(filtro)
        return queryset


class VacacionesCreateView(LoginRequiredMixin, BSModalCreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    template_name = 'empleado/vacaciones/forms/vacaciones.html'
    success_message = 'Nuevo registro dado de alta.'
    # success_url = reverse_lazy('rrhh:empl_vaca')

    def get_success_url(self):
        return reverse_lazy('rrhh:empl_vaca', args=(self.kwargs['empl_id'],))


class VacacionesUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Vacaciones
    template_name = 'empleado/vacaciones/forms/vacaciones.html'
    form_class = forms.VacacionesForm
    success_message = 'Registro actualizado correctamente.'

    def get_success_url(self):
        return reverse_lazy('rrhh:empl_vaca', args=(self.kwargs['empl_id'],))


class VacacionesDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = models.Vacaciones
    template_name = 'empleado/vacaciones/forms/confirmar_borrado.html'
    success_message = 'Registro eliminado correctamente.'

    def get_success_url(self):
        return reverse_lazy('rrhh:empl_vaca', args=(self.kwargs['empl_id'],))


def VacacionesAceptar(request, empl_id, pk):
    vaca = models.Vacaciones.objects.get(id=pk)
    vaca.estado = 'A'
    vaca.save()

    url = reverse_lazy('rrhh:empl_vaca', kwargs={'empl_id':empl_id})
    return redirect( url )


def VacacionesPendiente(request, empl_id, pk):
    vaca = models.Vacaciones.objects.get(id=pk)
    vaca.estado = 'P'
    vaca.save()

    url = reverse_lazy('rrhh:empl_vaca', kwargs={'empl_id':empl_id})
    return redirect( url )
