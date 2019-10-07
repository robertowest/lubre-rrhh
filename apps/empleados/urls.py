from django.urls import path

from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.index, name='index'),
    path('vacaciones/', views.index, name='vacaciones'),
    path('<int:empl_id>/vacaciones/', views.VacacionesCreateView.as_view(), name='vacaciones_create'),
    path('vacaciones/<int:pk>/modificar/', views.VacacionesUpdateView.as_view(), name='vacaciones_update'),
    path('vacaciones/<int:pk>/eliminar/', views.VacacionesDeleteView.as_view(), name='vacaciones_delete'),
]
