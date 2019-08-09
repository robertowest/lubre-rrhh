from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    # clientes
    path('', views.Listado.as_view(), name='show'),
    path('detalle/<int:pk>', views.Detalle.as_view(), name='detail'),
    path('crear', views.Crear.as_view(), name='create'),
    path('editar/<int:pk>', views.Editar.as_view(), name='edit'),
    path('eliminar/<int:pk>', views.Eliminar.as_view(), name='delete'),
    # actividades
    path('actividades/', views.Actividad_Listado.as_view(), name='act_show'),
    path('actividades/canal/<int:pk>', views.Actividad_Filtro.as_view(), name='act_filter'),
]
