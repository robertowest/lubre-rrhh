from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Comunicacion, Domicilio, Empleado, Persona

admin.site.register(Persona)
admin.site.register(Empleado)
admin.site.register(Comunicacion)
admin.site.register(Domicilio)
