from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Comunicacion, Domicilio, Empleado, Persona

admin.site.register(Persona)
admin.site.register(Comunicacion)
admin.site.register(Domicilio)

# class EmpleadoAdmin(admin.ModelAdmin):
#     list_display = ('persona', 'legajo', 'fec_ing', 'fec_egr')


class ComunicacionInline(admin.TabularInline):
    model = Comunicacion

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [ComunicacionInline,]

admin.site.register(Empleado, EmpleadoAdmin)
