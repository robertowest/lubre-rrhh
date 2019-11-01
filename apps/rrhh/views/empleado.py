from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
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
    model = models.Empleado
    template_name = 'empleado/detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tab'] = self.request.session['tab']
        # # context['comunicaciones'] = context['empleado'].comunicaciones.all()
        # context['domicilio'] = \
        #     models.Domicilio.objects.filter(empleado_id=context['empleado'].persona_id)
        # context['comunicaciones'] = \
        #     models.Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id).order_by('tipo')
        # # context['denuncias'] = models.Denuncia_ART.objects.filter(empleado_id=context['empleado'].persona_id)
        # # context['activos'] = models.ActivoMantenimientoView.objects.filter(responsable_id=context['empleado'].persona_id)
        return context


def EmpleadoDetailAjax(request):
    empleadoId = request.GET['pk']
    solapa = request.GET['tab']
    request.session['tab'] = solapa

    if solapa == 'datos':
        template = 'empleado/detalle/_info.html'
        info = models.Empleado.objects.get(persona_id=empleadoId)
        context = {'object': info}
        return render(request, template, context)
        # domi = models.Domicilio.objects.filter(empleado_id=empleadoId)

    elif solapa == 'denuncias':
        data = models.Denuncia_ART.objects.filter(empleado_id=empleadoId).filter(active=True)
        template = 'empleado/detalle/_denuncias.html'

    elif solapa == 'activos':
        data = models.Activo.objects.filter(responsable_id=empleadoId).filter(active=True)
        template = 'empleado/detalle/_activos.html'

    elif solapa == 'vacaciones':
        data = models.Vacaciones.objects.filter(empleado_id=empleadoId).filter(active=True)
        template = 'empleado/detalle/_vacaciones.html'

    return render(request, template, {'object_list': data, 'info_panel': 'panel'})


def EmpleadoDetailPanelAjax(request):
    empleadoId = request.GET['pk']

    if request.session['tab'] != 'vacaciones':
        data = models.Comunicacion.objects.filter(empleado_id=empleadoId).order_by('tipo')
        context = {'object_list': data }
        template = 'empleado/detalle/_info_panel.html'
    else:
        data = models.Empleado.objects.get(persona_id=empleadoId)
        context = {'empleado': data}
        template = 'empleado/detalle/_vacaciones_panel.html'

    return render(request, template, context)


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
        empleado = models.Empleado.objects.get(persona_id=self.kwargs['empl_id'])
        empleado.set_anio(self.kwargs['anio'])
        context = super().get_context_data(**kwargs)
        context['empl_id'] = self.kwargs['empl_id']
        context['anio'] = self.kwargs['anio']
        context['empleado'] = empleado
        return context

    def get_queryset(self):
        empl_id = self.kwargs['empl_id']
        anio    = self.kwargs['anio']
        # filtro = Q(empleado_id=empl_id) & Q(fec_inicio__year=anio) & Q(active=True)
        filtro = Q(empleado_id=empl_id) & Q(periodo=anio) & Q(active=True)
        queryset = models.Vacaciones.objects.filter(filtro)
        return queryset


class VacacionesCreateView(LoginRequiredMixin, BSModalCreateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    template_name = 'empleado/vacaciones/forms/vacaciones.html'
    success_message = 'Nuevo registro dado de alta.'
    # success_url = reverse_lazy('rrhh:empl_vaca')

    def form_valid(self, form):
        form.instance.periodo = self.kwargs['anio']
        return super(VacacionesCreateView, self).form_valid(form)

    def get_success_url(self):
        # return reverse_lazy('rrhh:empl_vaca', args=(self.kwargs['empl_id'], date.today().year))
        return reverse_lazy('rrhh:empl_detail', kwargs={'pk': self.kwargs['empl_id']})


class VacacionesUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Vacaciones
    form_class = forms.VacacionesForm
    template_name = 'empleado/vacaciones/forms/vacaciones.html'
    success_message = 'Registro actualizado correctamente.'

    def get_success_url(self):
        # return reverse_lazy('rrhh:empl_vaca', args=(self.kwargs['empl_id'], date.today().year))
        return reverse_lazy('rrhh:empl_detail', kwargs={'pk': self.kwargs['empl_id']})


class VacacionesDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = models.Vacaciones
    template_name = 'empleado/vacaciones/forms/confirmar_borrado.html'
    success_message = 'Registro eliminado correctamente.'

    def get_success_url(self):
        # return reverse_lazy('rrhh:empl_vaca', args=(self.kwargs['empl_id'], date.today().year))
        return reverse_lazy('rrhh:empl_detail', kwargs={'pk': self.kwargs['empl_id']})


def VacacionesAceptar(request, empl_id, pk):
    vaca = models.Vacaciones.objects.get(id=pk)
    vaca.estado = 'A'
    vaca.save()

    # url = reverse_lazy('rrhh:empl_vaca', kwargs={'empl_id':empl_id, 'anio':date.today().year})
    url = reverse_lazy('rrhh:empl_detail', kwargs={'pk': empl_id})
    return redirect( url )


def VacacionesPendiente(request, empl_id, pk):
    vaca = models.Vacaciones.objects.get(id=pk)
    vaca.estado = 'P'
    vaca.save()

    # url = reverse_lazy('rrhh:empl_vaca', kwargs={'empl_id':empl_id, 'anio':date.today().year})
    url = reverse_lazy('rrhh:empl_detail', kwargs={'pk': empl_id})
    return redirect( url )


def AsignarVacaciones(request, anio):
    f_inicio = date(anio, date.today().month, date.today().day) - relativedelta(months=14)
    f_fin = date(anio, 12, 31)

    persona = models.Persona()
    persona.nombre = 'Diego'
    persona.apellido = 'Maradona'

    empleado = models.Empleado()
    empleado.persona = persona
    empleado.fec_ing = f_inicio

    tot = empleado.vacaciones['totales']
    hab = empleado.vacaciones['habiles']

    valores = {'fecha_inicio': f_inicio,
               'periodo': anio,
               'fecha_fin': f_fin,
               'dias_totales': tot,
               'dias_habiles': hab,
               'empleado': empleado}

    return render(request, 'empleado/vacaciones/asignacion.html', {'data': valores})


def CalcularVacaciones(request, anio):
    # anio = date.today().year

    # obtenemos todos los registros activos con fecha de ingreso informada
    # filtro = Q(created__year=2018)
    filtro = Q(fec_ing__isnull=False) & Q(active=True)
    empleados = models.Empleado.objects.filter(filtro)

    # calculamos la información para el año 2018
    for empleado in empleados:
        x = date(anio, 12, 31)

        if (empleado.fec_ing != None):
            trabajado = int((x - empleado.fec_ing).days / 365)
            if trabajado >= 1 and trabajado < 5:
                total = 14
            elif trabajado >= 5 and trabajado < 10:
                total = 21
            elif trabajado >= 10 and trabajado < 20:
                total = 28
            elif trabajado >= 20:
                total = 35
            else:
                if empleado.fec_ing.month < 7:
                    total = 14
                else:
                    total = int((x - empleado.fec_ing).days / 30)

        if total > 0:
            vaca = models.DiasVacaciones()
            vaca.empleado = empleado
            vaca.periodo = anio
            vaca.dias_vacaciones = total
            vaca.dias_disfrutados = 0
            vaca.dias_pendientes = 0
            vaca.save()

    return HttpResponse('Se cargaron los días de vacaciones para el año {{anio}}')


# def get_progress(request, task_id):
#     result = AsyncResult(task_id)
#     response_data = {
#         'state': result.state,
#         'details': result.info,
#     }
#     return HttpResponse(json.dumps(response_data), content_type='application/json')

class VacacionesView(ListView, FormView):
    model = models.Vacaciones
    form_class = forms.VacacionesFiltro
    template_name = 'vacaciones/grafico.html'

    def get_context_data(self, **kwargs):
        # datos = super(VacacionesView, self).get_queryset().filter(periodo=2019).order_by('fec_inicio')
        datos = super(VacacionesView, self).get_context_data()['object_list']

        dataSource = []
        for dato in datos:
            dataSource.append({'category': dato.empleado.persona.apellido,
                               'start': dato.fec_inicio.strftime('%Y-%m-%d'),
                               'end': dato.fec_fin.strftime('%Y-%m-%d'),
                               'color': ('green' if dato.estado == 'A' else 'red'),
                               'task': dato.empleado.persona.nombre})

        context = super(VacacionesView, self).get_context_data(**kwargs)
        context['parametro'] = dataSource
        return context

    def get_queryset(self):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            queryset = super(VacacionesView, self).get_queryset().order_by('fec_inicio')
        else:
            queryset = super(VacacionesView, self).get_queryset()\
                .filter(periodo=form.fields['periodo'].initial)\
                .filter(active=True).order_by('fec_inicio')
        return queryset

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            if form.cleaned_data['empleado']:
                self.object_list = self.object_list.filter(empleado=form.cleaned_data['empleado'])
            if form.cleaned_data['periodo']:
                self.object_list = self.object_list.filter(periodo=form.cleaned_data['periodo'])
            if form.cleaned_data['estado']:
                self.object_list = self.object_list.filter(estado=form.cleaned_data['estado'])
            if form.cleaned_data['mes']:
                self.object_list = self.object_list.filter(fec_inicio__month=form.cleaned_data['mes'])
            self.object_list = self.object_list.filter(active=True).order_by('fec_inicio')
        return self.render_to_response(self.get_context_data(object_list=self.object_list, form=form))


class VacacionesListadoView(ListView, FormView):
    model = models.Vacaciones
    form_class = forms.VacacionesFiltro
    template_name = 'vacaciones/listado.html'

    def get_queryset(self):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            queryset = super(VacacionesListadoView, self).get_queryset().order_by('fec_inicio')
        else:
            queryset = super(VacacionesListadoView, self).get_queryset()\
                .filter(periodo=form.fields['periodo'].initial)\
                .filter(active=True).order_by('fec_inicio')
        # return queryset.order_by('persona')
        # queryset = models.Vacaciones.objects.filter(active=True)
        return queryset

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            if form.cleaned_data['empleado']:
                self.object_list = self.object_list.filter(empleado=form.cleaned_data['empleado'])
            if form.cleaned_data['periodo']:
                self.object_list = self.object_list.filter(periodo=form.cleaned_data['periodo'])
            if form.cleaned_data['estado']:
                self.object_list = self.object_list.filter(estado=form.cleaned_data['estado'])
            if form.cleaned_data['mes']:
                self.object_list = self.object_list.filter(fec_inicio__month=form.cleaned_data['mes'])
            self.object_list = self.object_list.filter(active=True).order_by('fec_inicio')
        return self.render_to_response(self.get_context_data(object_list=self.object_list, form=form))
