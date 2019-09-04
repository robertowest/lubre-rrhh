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
    path('doc_man_ajax/', views.doc_man_ajax, name='doc_man_ajax'),             # documento-mantenimiento
    path('act_man_ajax/', views.act_man_ajax, name='act_man_ajax'),             # actividad-mantenimiento
    path('act_doc_ajax/', views.act_doc_ajax, name='act_doc_ajax'),             # actividad-documento
    path('act_doc_man_ajax/', views.act_doc_man_ajax, name='act_doc_man_ajax'), # actividad-documento-mantenimiento

    # documentación
    path('asignacion/<int:empl_id>/documento/nuevo',
         views.DocumentacionCreateView.as_view(), name='doc_create'),
    path('asignacion/<int:empl_id>/documento/editar/<int:pk>',
         views.DocumentacionUpdateView.as_view(), name='doc_update'),

    # activo
    path('asignacion/<int:empl_id>/activo/nuevo', views.ActivoCreateView.as_view(), name='act_create'),
]
