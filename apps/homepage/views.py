from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.rrhh.models import Empleado

# Create your views here.
def home(request):
    url = a_donde_voy(request)
    return HttpResponseRedirect(url)


def example(request):
    return render(request, 'homepage.html')


def demo(request):
    return render(request, 'demo.html')


def modal(request):
    return render(request, 'modal.html')


def a_donde_voy(request):
    if request.user.is_anonymous:
        url = reverse('rrhh:empl_index')

    else:
        # obtenemos todos los grupos del usuario
        groups = request.user.groups.filter(user=request.user)

        if groups:
            group = groups[0]   # seleccionamos el grupo principal

            if group.name == "Empleados":
                # usuario = request.user
                # empleado = Empleado.objects.get(user_id=usuario.id)
                # url = reverse('rrhh:empl_detail', kwargs={'pk': empleado.persona.id})
                url = reverse('rrhh:empl_index')

            elif group.name == "RRHH":
                url = reverse('rrhh:home')

            else:
                url = reverse('rrhh:empl_index')

    return url
