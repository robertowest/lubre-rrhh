from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('example/', views.example, name='example'),
    path('demo/', views.demo, name='demo'),
    path('modal/', views.modal, name='modal'),
]
