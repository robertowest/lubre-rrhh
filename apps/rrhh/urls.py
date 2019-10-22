from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'rrhh'

urlpatterns = [
    path('', views.home, name='home'),

    path('empleado/', views.index, name='empl_index'),

    # CRUD empleado
    path('empleado/listado/', views.EmpleadoShow.as_view(), name='empl_show'),
    path('empleado/nuevo/', views.EmpleadoCreate.as_view(), name='empl_new'),
    path('empleado/editar/<int:pk>', views.EmpleadoUpdate.as_view(), name='empl_edit'),
    path('empleado/eliminar/<int:pk>', views.EmpleadoDelete.as_view(), name='empl_delete'),

    # detalle del empleado
    path('empleado/detalle/<int:pk>', views.EmpleadoDetail.as_view(), name='empl_detail'),

    # vacaciones
    path('empleado/<int:empl_id>/vacaciones/<int:anio>/', views.VacacionesReadView.as_view(), name='empl_vaca'),
    path('empleado/<int:empl_id>/vacaciones/solicitar/<int:anio>/', views.VacacionesCreateView.as_view(), name='empl_vaca_create'),
    path('empleado/<int:empl_id>/vacaciones/modificar/<int:pk>/', views.VacacionesUpdateView.as_view(), name='empl_vaca_update'),
    path('empleado/vacaciones/eliminar/<int:pk>/', views.VacacionesDeleteView.as_view(), name='empl_vaca_delete'),

    path('empleado/<int:empl_id>/vacaciones/aceptar/<int:pk>/', views.VacacionesAceptar, name='empl_vaca_aceptar'),
    path('empleado/<int:empl_id>/vacaciones/pendiente/<int:pk>/', views.VacacionesPendiente, name='empl_vaca_pendiente'),

    path('empleado/asignar/vacaciones/<int:anio>/', views.AsignarVacaciones, name='empl_vaca_asignar'),
    path('empleado/calcular/vacaciones/<int:anio>/', views.CalcularVacaciones, name='empl_vaca_calcular'),
    # path('<task_id>', views.get_progress, name='task_status'),

    # canales de comunicacion
    path('canal/nuevo/', views.CanalCreate.as_view(), name='canal_new'),

    # denuncias
    path('<int:empl_id>/denuncia/nueva/', views.DenunciaCreateView.as_view(), name='art_create'),
    path('<int:empl_id>/denuncia/info/<int:pk>', views.DenunciaReadView.as_view(), name='art_read'),
    path('<int:empl_id>/denuncia/editar/<int:pk>', views.DenunciaUpdateView.as_view(), name='art_update'),
    path('<int:empl_id>/denuncia/eliminar/<int:pk>', views.DenunciaDeleteView.as_view(), name='art_delete'),

    # lectura de registros
    path('activo/info/<int:pk>', views.ActivoReadView.as_view(), name='activo_read'),
    path('mantenimiento/info/<int:pk>', views.MantenimientoReadView.as_view(), name='mantenimiento_read'),
    # login_required(views.MantenimientoCheckView.as_view())
    path('mantenimiento/editar/<int:pk>', views.MantenimientoCheckView.as_view(),
                                          name='mantenimiento_check'),
    path('noticia/<slug:slug>/', views.PostReadView.as_view(), name='post_detail'),

    # asignaciones
    path('asignacion/<int:empl_id>', views.asignacion, name='asignacion'),
    path('asignacion/<int:empl_id>/activo/<int:activo_id>', views.activo, name='activo'),

    # activo
    path('asignacion/<int:empl_id>/activo/nuevo', views.ActivoCreateView.as_view(), name='activo_create'),
    path('asignacion/<int:empl_id>/activo/editar/<int:pk>', views.ActivoUpdateView.as_view(), name='activo_update'),
    # mantenimiento de activo
    path('asignacion/<int:empl_id>/activo/<int:activo_id>/nuevo', views.MantenimientoCreateView.as_view(),
                                                                  name='mantenimiento_create'),
    path('asignacion/<int:empl_id>/activo/<int:activo_id>/editar/<int:pk>', views.MantenimientoUpdateView.as_view(),
                                                                            name='mantenimiento_update'),

    # listado de vacaciones
    path('vacaciones/', views.VacacionesView.as_view(), name='vaca_index'),
]
