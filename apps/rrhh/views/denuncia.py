from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.rrhh import models, forms


class DenunciaCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'denuncia/formulario.html'
    form_class = forms.DenunciaForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('rrhh:empl_show')


class DenunciaUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = models.Denuncia_ART
    template_name = 'denuncia/formulario.html'
    form_class = forms.DenunciaForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('rrhh:empl_show')


class DenunciaReadView(LoginRequiredMixin, BSModalReadView):
    model = models.Denuncia_ART
    template_name = 'denuncia/detalle.html'


class DenunciaDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = models.Denuncia_ART
    template_name = 'denuncia/confirmar_borrado.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('rrhh:empl_show')