from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from apps.rrhh.models import Empleado, Vacaciones
from .forms import VacacionesForm


def index(request):
    empleado = None
    vacaciones = None

    if not request.user.is_anonymous:
        usuario = request.user
        empleado = Empleado.objects.get(user_id=usuario.id)
        vacaciones = Vacaciones.objects.filter(empleado_id=empleado.persona_id)

    return render(request, 'empleados/index.html', {'object': empleado, 'vacaciones': vacaciones})


class VacacionesCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'empleados/forms/vacaciones.html'
    form_class = VacacionesForm

    def get_success_url(self):
        return reverse_lazy('empleados:index', kwargs={'empl_id': self.kwargs['empl_id']})

