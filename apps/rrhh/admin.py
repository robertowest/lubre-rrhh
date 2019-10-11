from datetime import datetime
from django.contrib import admin

# Register your models here.
from . import models


class PersonaAdmin(admin.ModelAdmin):
    def fld_persona(self, obj):
        return '{}, {}'.format(obj.apellido, obj.nombre)
    fld_persona.admin_order_field = ['apellido', 'nombre']  # ordenado
    fld_persona.short_description = 'Nombre'

    list_display = ['fld_persona', 'dni']
    list_filter = ['active']
    search_fields = ['apellido', 'nombre']
    list_per_page = 20


admin.site.register(models.Persona, PersonaAdmin)


class ComunicacionAdmin(admin.ModelAdmin):
    def fld_empleado(self, obj):
        return '{}, {}'.format(obj.empleado.persona.apellido, obj.empleado.persona.nombre)
    # fld_empleado.admin_order_field = 'empleado'  # ordenado
    fld_empleado.short_description = 'Empleado'

    list_display = ['fld_empleado', 'tipo', 'texto', 'active']
    list_display_links = ['texto']
    list_filter = ['active']
    search_fields = ['empleado__persona__apellido', 'empleado__persona__nombre']
    list_per_page = 20


admin.site.register(models.Comunicacion, ComunicacionAdmin)


class DomicilioAdmin(admin.ModelAdmin):
    def fld_empleado(self, obj):
        return '{}, {}'.format(obj.empleado.persona.apellido, obj.empleado.persona.nombre)
    fld_empleado.admin_order_field = 'empleado'   # ordenado
    fld_empleado.short_description = 'Empleado'

    list_display = ['fld_empleado', 'domicilio', 'localidad', 'provincia', 'cp', 'active']
    search_fields = ['empleado__persona__apellido', 'empleado__persona__nombre']
    list_display_links = ['domicilio']

admin.site.register(models.Domicilio, DomicilioAdmin)


class ComunicacionInline(admin.TabularInline):
    model = models.Comunicacion


class EmpleadoAdmin(admin.ModelAdmin):
    def fld_persona(self, obj):
        return '{}, {}'.format(obj.persona.apellido, obj.persona.nombre)
    fld_persona.admin_order_field = 'persona'   # ordenado
    fld_persona.short_description = 'Nombre'

    # def fld_apellido(self, obj):
    #     return obj.persona.apellido
    # fld_apellido.admin_order_field = 'persona'   # ordenado
    # fld_apellido.short_description = 'Apellido'
    #
    # def fld_nombre(self, obj):
    #     return obj.persona.nombre
    # fld_nombre.short_description = 'Nombre'

    def fld_ingreso(self, obj):
        if obj.fec_ing == None:
            return ""
        return obj.fec_ing.strftime("%d/%m/%Y")
    fld_ingreso.short_description = 'F.Ingreso'

    def fld_egreso(self, obj):
        if obj.fec_egr == None:
            return ""
        return obj.fec_egr.strftime("%d/%m/%Y")
    fld_egreso.short_description = 'F.Egreso'

    model = models.Empleado
    list_filter = ['active']
    list_display = ['fld_persona', 'legajo', 'fld_ingreso', 'fld_egreso', 'active']
    search_fields = ['persona__apellido', 'persona__nombre']
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
    list_display = ('descripcion', 'responsable')
    list_filter = ('tipo',)
    list_per_page = 20


admin.site.register(models.Activo, ActivoAdmin)


class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'activo', 'estado', 'proximo', 'fecha_inicial', 'fecha_final')
    list_filter = ('activo', 'estado', )
    search_fields=('descripcion', )
    list_per_page = 20


admin.site.register(models.Mantenimiento, MantenimientoAdmin)


# -------------------------------------------------------------------
# Calendario
# -------------------------------------------------------------------

class FeriadoAdmin(admin.ModelAdmin):
    def fld_fecha_larga(self, obj):
        return obj.fecha.strftime("%A, %d %B %Y")
    fld_fecha_larga.short_description = 'Fecha Larga'

    date_hierarchy = 'fecha'
    list_display = ('fecha', 'descripcion', 'fld_fecha_larga')
    list_per_page = 20


admin.site.register(models.Feriados, FeriadoAdmin)


admin.site.register(models.Tarea)