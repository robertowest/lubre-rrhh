"""
Controla el estado de los mantenimientos de RRHH.
"""
from datetime import timedelta
from django.db.models import Q
from django.utils import timezone

from apps.rrhh.models import Mantenimiento

# def run():
#     # recupera todos los registros
#     mantenimientos = Mantenimiento.objects.all()
#     # los muestra por pantalla
#     for m in mantenimientos:
#         print(m)


def run():
    # recupera los mantenimientos con vencimiento en los pŕoximos 7 días
    f1 = Q(proximo__range=(timezone.now() + timedelta(days=1),
                           timezone.now() + timedelta(days=7)))
    f2 = Q(fecha_final__range=(timezone.now() + timedelta(days=1),
                               timezone.now() + timedelta(days=7)))
    proximos = Mantenimiento.objects.filter(f1 | f2)

    # vencidas
    v1 = Q(proximo__lt=timezone.now()) | Q(fecha_final__lt=timezone.now())
    vencidos = Mantenimiento.objects.filter(v1)

    # modificamos el estado
    # SEMAFORO = [(None, '---'), ('R', 'No Cumple'), ('A', 'Atención'), ('V', 'Cumple')]
    for m in proximos:
        m.estado = 'A'
        m.save()

    for m in vencidos:
        m.estado = 'R'
        m.save()
