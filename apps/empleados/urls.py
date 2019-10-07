from django.urls import path

from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.index, name='index'),
    path('vacaciones/', views.index, name='vacaciones'),
    path('<int:empl_id>/vacaciones/solicitar/', views.VacacionesCreateView.as_view(), name='vacaciones_create'),
]
