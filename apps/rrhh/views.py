from betterforms.multiform import MultiModelForm
from bootstrap_modal_forms.generic import \
    BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView

from . import models
from .forms import DenunciaForm, EmpleadoMultiForm, ComunicacionForm, EmpleadoFiltro

# from django.contrib.auth.decorators import login_required
# @login_required
# def index(request):
#     pass

def home(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    # vencimientos = Documentacion.objects.all()  # filter('dias_vencido': 0)

    # Model.objects.filter(Q(x=1) & Q(y=2))
    # vencimientos = Documentacion.objects.filter(Q(dias_vencido='0'))
    mantenimientos = models.Mantenimiento.objects.filter(proximo__lt=timezone.now())
    vencimientos = models.Documentacion.objects.filter(fecha_final__lt=timezone.now())
    return render(request, 'rrhh_home.html', {'mantenimientos': mantenimientos,
                                              'vencimientos': vencimientos})


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

    model = models.Empleado
    form_class = EmpleadoFiltro
    template_name = 'empleado/listado.html'
    paginate_by = 25
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoDetail(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comunicaciones'] = context['empleado'].comunicaciones.all()
        context['domicilio'] = \
            models.Domicilio.objects.filter(empleado_id=context['empleado'].persona_id)
        context['comunicaciones'] = \
            models.Comunicacion.objects.filter(empleado_id=context['empleado'].persona_id).order_by('tipo')
        context['denuncias'] = models.Denuncia_ART.objects.filter(empleado_id=context['empleado'].persona_id)
        # context['activos'] = models.Activo.objects.filter(responsable_id=context['empleado'].persona_id)
        context['activos'] = models.ActivoMantenimientoView.objects.filter(responsable_id=context['empleado'].persona_id)
        return context

    model = models.Empleado
    # form_class = Empleado
    template_name = 'empleado/detalle.html'
    # template_name = 'empleado/activos.html'


class EmpleadoCreate(LoginRequiredMixin, CreateView):
    login_url = '/usuarios/inicio/'
    form_class = EmpleadoMultiForm
    template_name = 'empleado/formulario.html'
    success_url = reverse_lazy('rrhh:empl_show')


class EmpleadoUpdate(UpdateView):
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


# -------------------------------------------------------------------


class DenunciaCreateView(BSModalCreateView):
    template_name = 'denuncia/formulario.html'
    form_class = DenunciaForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('rrhh:empl_show')


class DenunciaUpdateView(BSModalUpdateView):
    model = models.Denuncia_ART
    template_name = 'denuncia/formulario.html'
    form_class = DenunciaForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('rrhh:empl_show')


class DenunciaReadView(BSModalReadView):
    model = models.Denuncia_ART
    template_name = 'denuncia/detalle.html'


class DenunciaDeleteView(BSModalDeleteView):
    model = models.Denuncia_ART
    template_name = 'denuncia/confirmar_borrado.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('rrhh:empl_show')


# -------------------------------------------------------------------


class ActivoReadView(BSModalReadView):
    model = models.Activo
    template_name = 'comunes/detalle.html'


class DocumentacionReadView(BSModalReadView):
    model = models.Documentacion
    template_name = 'comunes/detalle.html'


class MantenimientoReadView(BSModalReadView):
    model = models.Mantenimiento
    template_name = 'comunes/detalle.html'
