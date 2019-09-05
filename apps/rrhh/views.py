from betterforms.multiform import MultiModelForm
from bootstrap_modal_forms.generic import \
    BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView


from . import models, forms
from apps.blog.models import Post

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
    # noticias = Post.objects.filter(estado=1).order_by('-created')
    noticias = Post.objects.all().order_by('-created')
    return render(request, 'rrhh/home.html', {'mantenimientos': mantenimientos,
                                              'noticias': noticias,
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
    form_class = forms.EmpleadoFiltro
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
    form_class = forms.EmpleadoMultiForm
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
    form_class = forms.EmpleadoMultiForm
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
    form_class = forms.ComunicacionForm
    template_name = 'comunicacion/formulario.html'


# -------------------------------------------------------------------


class DenunciaCreateView(BSModalCreateView):
    template_name = 'denuncia/formulario.html'
    form_class = forms.DenunciaForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('rrhh:empl_show')


class DenunciaUpdateView(BSModalUpdateView):
    model = models.Denuncia_ART
    template_name = 'denuncia/formulario.html'
    form_class = forms.DenunciaForm
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
    template_name = 'comunes/read-modal.html'


class DocumentacionReadView(BSModalReadView):
    model = models.Documentacion
    template_name = 'comunes/read-modal.html'


class MantenimientoReadView(BSModalReadView):
    model = models.Mantenimiento
    template_name = 'comunes/read-modal.html'


class PostReadView(BSModalReadView):
    model = Post
    template_name = 'comunes/read-modal.html'


# -------------------------------------------------------------------


def asignacion(request, pk):
    context = {'Empleado': models.Empleado.objects.get(persona_id=pk),
               'Doc': models.Documentacion.objects.filter(responsable_id=pk), 'DocMan': None,
               'Act': models.Activo.objects.filter(responsable_id=pk),
               'ActMan': None, 'ActDoc': None, 'ActDocMan': None,
               'referencia': pk}
    return render(request, 'asignacion/index.html', context)

def doc_man_ajax(request):
    pk = request.GET.get('id', None)
    context = {'DocMan': models.Mantenimiento.objects.filter(object_id=pk),
               'referencia': pk}
    return render(request, 'asignacion/ajax/doc_man_ajax.html', context)

def act_man_ajax(request):
    pk = request.GET.get('id', None)
    context = {'ActMan': models.Mantenimiento.objects.filter(object_id=pk),
               'referencia': pk}
    return render(request, 'asignacion/ajax/act_man_ajax.html', context)

def act_doc_ajax(request):
    pk = request.GET.get('id', None)
    context = {'ActDoc': models.Documentacion.objects.filter(activo_id=pk),
               'referencia': pk}
    return render(request, 'asignacion/ajax/act_doc_ajax.html', context)

def act_doc_man_ajax(request):
    # import pdb; pdb.set_trace()
    pk = request.GET.get('id', None)
    # content_type_id = 30  --> documentacion
    # content_type_id = 32  --> mantenimiento
    context = {'ActDocMan': models.Mantenimiento.objects.filter(content_type_id=30, object_id=pk),
               'referencia': pk}
    return render(request, 'asignacion/ajax/act_doc_man_ajax.html', context)


# -------------------------------------------------------------------


class DocumentacionCreateView(BSModalCreateView):
    form_class = forms.DocumentoForm
    template_name = 'asignacion/forms/doc_form.html'

    def get_success_url(self):
        return reverse_lazy('rrhh:asignacion', kwargs={'pk': self.kwargs['empl_id']})

    # def get_form_kwargs(self):
    #     if 'empl_id' in self.kwargs:
    #         kwargs = super(DocumentacionCreateView, self).get_form_kwargs()
    #         kwargs.update({'empleado_id': self.kwargs['empl_id']})
    #     return kwargs


class DocumentacionUpdateView(BSModalUpdateView):
    model = models.Documentacion
    template_name = 'asignacion/forms/doc_form.html'
    form_class = forms.DocumentoForm
    success_message = 'La documentación fue correctamente actualizada.'

    def get_success_url(self):
        return reverse_lazy('rrhh:asignacion', kwargs={'pk': self.kwargs['empl_id']})


class ActivoCreateView(BSModalCreateView):
    form_class = forms.ActivoForm
    template_name = 'asignacion/forms/act_form.html'

    def get_success_url(self):
        return reverse_lazy('rrhh:asignacion', kwargs={'pk': self.kwargs['empl_id']})

    def get_form_kwargs(self):
        '''pasamos el valor de una variable al formulario'''
        import pdb; pdb.set_trace()
        kwargs = super().get_form_kwargs()
        kwargs.update({'empleado_id': self.kwargs['empl_id']})
        return kwargs


class ActivoUpdateView(BSModalUpdateView):
    model = models.Activo
    template_name = 'asignacion/forms/act_form.html'
    form_class = forms.ActivoForm
    success_message = 'El activo fue correctamente actualizado.'

    def get_success_url(self):
        return reverse_lazy('rrhh:asignacion', kwargs={'pk': self.kwargs['empl_id']})
