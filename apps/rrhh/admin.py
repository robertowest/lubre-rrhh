from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Persona)
admin.site.register(models.Comunicacion)
admin.site.register(models.Domicilio)

# class EmpleadoAdmin(admin.ModelAdmin):
#     list_display = ('persona', 'legajo', 'fec_ing', 'fec_egr')


class ComunicacionInline(admin.TabularInline):
    model = models.Comunicacion

class EmpleadoAdmin(admin.ModelAdmin):
    inlines = [ComunicacionInline,]

admin.site.register(models.Empleado, EmpleadoAdmin)


class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('siniestro', 'empleado', 'fec_alta_medica')

admin.site.register(models.Diccionario_ART)
admin.site.register(models.Denuncia_ART, DenunciaAdmin)


# -------------------------------------------------------------------
# CONFIGURACION PARA USAR EN ADMIN
# -------------------------------------------------------------------

class ActivoAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'tipo', 'responsable')
    list_filter = ('tipo',)

admin.site.register(models.Activo, ActivoAdmin)

class DocumentacionAdmin(admin.ModelAdmin):
    list_display = ('activo', 'descripcion', 'fecha_inicial', 'fecha_final')
    list_filter = ('activo',)

admin.site.register(models.Documentacion, DocumentacionAdmin)

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'descripcion', 'estado', 'proximo')
    list_filter = ('estado',)

admin.site.register(models.Mantenimiento, MantenimientoAdmin)
