from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from apps.rrhh.models import Empleado, Vacaciones
from .forms import VacacionesForm
from apps.rrhh.models import Vacaciones


def index(request):
    empleado = None
    vacaciones = None

    if not request.user.is_anonymous:
        usuario = request.user
        empleado = Empleado.objects.get(user_id=usuario.id)
        filtro = Q(empleado_id=empleado.persona_id) & Q(active=True)
        vacaciones = Vacaciones.objects.filter(filtro)

    return render(request, 'empleados/index.html', {'object': empleado, 'vacaciones': vacaciones})


class VacacionesCreateView(LoginRequiredMixin, BSModalCreateView):
    form_class = VacacionesForm
    template_name = 'empleados/forms/vacaciones.html'
    success_message = 'Nuevo registro dado de alta.'
    success_url = reverse_lazy('empleados:index')


class VacacionesUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Vacaciones
    template_name = 'empleados/forms/vacaciones.html'
    form_class = VacacionesForm
    success_message = 'Registro actualizado correctamente.'
    success_url = reverse_lazy('empleados:index')


class VacacionesDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Vacaciones
    template_name = 'empleados/forms/confirmar_borrado.html'
    success_message = 'Registro eliminado correctamente.'
    success_url = reverse_lazy('empleados:index')
