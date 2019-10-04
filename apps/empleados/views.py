from django.shortcuts import render

from apps.rrhh.models import Empleado, Vacaciones

def index(request):
    empleado = None
    vacaciones = None

    if not request.user.is_anonymous:
        usuario = request.user
        empleado = Empleado.objects.get(persona_id=usuario.id)
        vacaciones = Vacaciones.objects.filter(empleado=usuario.id)

    return render(request, 'empleados/index.html', {'object': empleado, 'vacaciones': vacaciones})

