from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Empleado


def home(request):
    return render(request, 'rrhh_home.html')


class EmpleadoShow(ListView):
    model = Empleado
    template_name = 'empleado/listado.html'
    paginate_by = 25


class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = 'empleado/detalle.html'