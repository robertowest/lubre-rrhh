from django.contrib import admin

# Register your models here.
from .models import Comunicacion, Denuncia_ART, Diccionario_ART, Domicilio, Empleado, Persona

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


class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('siniestro', 'empleado', 'fec_alta_medica')

admin.site.register(Diccionario_ART)
admin.site.register(Denuncia_ART, DenunciaAdmin)

# ----------------------------------------------------------------

from .models import Activo, Documentacion, Mantenimiento

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'identificacion', 'responsable')
    list_filter = ('tipo',)

admin.site.register(Activo, ActivoAdmin)

class DocumentacionAdmin(admin.ModelAdmin):
    list_display = ('activo', 'descripcion', 'fecha_inicial', 'fecha_final')
    list_filter = ('activo',)

admin.site.register(Documentacion, DocumentacionAdmin)

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'descripcion', 'estado', 'proximo')
    list_filter = ('estado',)

admin.site.register(Mantenimiento, MantenimientoAdmin)
