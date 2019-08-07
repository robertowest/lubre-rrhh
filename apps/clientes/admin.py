from django.contrib import admin

# Register your models here.
from .models import Actividades, Califica, Estadocliente, Clientes

admin.site.register(Actividades)
admin.site.register(Califica)
admin.site.register(Estadocliente)
admin.site.register(Clientes)
