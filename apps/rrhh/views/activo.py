from bootstrap_modal_forms.generic import BSModalReadView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.rrhh import models

class ActivoReadView(LoginRequiredMixin, BSModalReadView):
    model = models.Activo
    template_name = 'comunes/read-modal.html'


class MantenimientoReadView(LoginRequiredMixin, BSModalReadView):
    model = models.Mantenimiento
    template_name = 'comunes/read-modal.html'
