from django.urls import path

from . import views

app_name = 'rrhh'

urlpatterns = [
    path('', views.home, name='home'),

    # CRUD empleado
    path('empleado/', views.EmpleadoShow.as_view(), name='empl_show'),
    path('empleado/detalle/<int:pk>', views.EmpleadoDetail.as_view(), name='empl_detail'),
    path('empleado/nuevo/', views.EmpleadoCreate.as_view(), name='empl_new'),
    path('empleado/editar/<int:pk>', views.EmpleadoUpdate.as_view(), name='empl_edit'),
    path('empleado/eliminar/<int:pk>', views.EmpleadoDelete.as_view(), name='empl_delete'),

    # canales de comunicacion
    path('canal/nuevo/', views.CanalCreate.as_view(), name='canal_new'),

    # denuncias
    path('denuncia/nueva/', views.DenunciaCreateView.as_view(), name='art_create'),
    path('denuncia/editar/<int:pk>', views.DenunciaUpdateView.as_view(), name='art_update'),
    path('denuncia/info/<int:pk>', views.DenunciaReadView.as_view(), name='art_read'),
    path('denuncia/eliminar/<int:pk>', views.DenunciaDeleteView.as_view(), name='art_delete'),

    # lectura de registros
    path('activo/info/<int:pk>', views.ActivoReadView.as_view(), name='activo_read'),
    path('documentacion/info/<int:pk>', views.DocumentacionReadView.as_view(), name='documentacion_read'),
    path('mantenimiento/info/<int:pk>', views.MantenimientoReadView.as_view(), name='mantenimiento_read'),
    path('noticia/<slug:slug>/', views.PostReadView.as_view(), name='post_detail'),

    # asignaciones
    path('asignacion/<int:pk>', views.asignacion, name='asignacion'),
    path('act_man_ajax/', views.act_man_ajax, name='act_man_ajax'),

    # path('detalle/<int:pk>', views.Detalle.as_view(), name='detail'),
    # path('crear', views.Crear.as_view(), name='create'),
    # path('editar/<int:pk>', views.Editar.as_view(), name='edit'),
    # path('eliminar/<int:pk>', views.Eliminar.as_view(), name='delete'),
    # # actividades
    # path('actividades/', views.Actividad_Listado.as_view(), name='act_show'),
    # path('actividades/canal/<int:pk>', views.Actividad_Filtro.as_view(), name='act_filter'),
]
