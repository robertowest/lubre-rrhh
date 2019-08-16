from django.urls import path

from . import views

app_name = 'rrhh'

urlpatterns = [
    path('', views.home, name='home'),
    # empleados
    path('empleado/', views.EmpleadoShow.as_view(), name='empl_show'),
    path('empleado/detalle/<int:pk>', views.EmpleadoDetail.as_view(), name='empl_detail'),
    path('empleado/nuevo/', views.EmpleadoCreate.as_view(), name='empl_new'),
    path('empleado/editar/<int:pk>', views.EmpleadoUpdate.as_view(), name='empl_edit'),
    path('empleado/eliminar/<int:pk>', views.EmpleadoDelete.as_view(), name='empl_delete'),

    path('canal/nuevo/', views.CanalCreate.as_view(), name='canal_new'),

    # path('detalle/<int:pk>', views.Detalle.as_view(), name='detail'),
    # path('crear', views.Crear.as_view(), name='create'),
    # path('editar/<int:pk>', views.Editar.as_view(), name='edit'),
    # path('eliminar/<int:pk>', views.Eliminar.as_view(), name='delete'),
    # # actividades
    # path('actividades/', views.Actividad_Listado.as_view(), name='act_show'),
    # path('actividades/canal/<int:pk>', views.Actividad_Filtro.as_view(), name='act_filter'),
]
