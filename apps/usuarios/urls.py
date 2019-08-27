from django.urls import path

# agregamos acciones de usuarios (login,logout)
from django.contrib.auth import views as auth_views

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('salir/', auth_views.LogoutView.as_view(),  {'next_page': '/'}, name='logout'),
    path('cambiar_clave/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='reset_password'),
    # agregamos acciones propias
    path('registro/', views.register, name='register'),
    path('perfil/', views.profile, name='profile'),
]
