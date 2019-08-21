from django.utils import timezone
from django.db import models
from django.urls import reverse_lazy

from apps.comunes.models import AudtoriaMixin


class Persona(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

    SEXO = (('M', 'Masculino'), ('F', 'Femenino'))

    apellido = models.CharField(max_length=30, blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=True, null=True)
    cuil = models.CharField(max_length=13, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    fec_nac = models.DateField(blank=True, null=True)


class Tarea(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.descripcion

    descripcion = models.CharField(max_length=40, blank=False, null=False)


class Empleado(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['persona__apellido', 'persona__nombre']

    def __str__(self):
        return '{}, {}'.format(self.persona.apellido, self.persona.nombre)

    def get_absolute_url(self, *args, **kwargs):
        # return reverse('rrhh:empl_detail', kwargs={'pk': self.pk})
        return reverse_lazy('rrhh:empl_detail', args=(self.pk,))

    # def get_success_url(self):
    #     # return reverse('rrhh:empl_detail', args=(self.object.id,))
    #     return reverse('rrhh:empl_show')
    #
    # def get_update_url(self):
    #     return reverse('rrhh:empl_edit', args=(self.pk,))
    #
    # def get_delete_url(self):
    #     return reverse('rrhh:empl_delete', args=(self.pk,))

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    legajo = models.CharField(max_length=4, blank=False, null=False)
    fec_ing = models.DateField('Fecha Ingreso', blank=True, null=True)
    fec_egr = models.DateField('Fecha Egreso',blank=True, null=True)
    imagen = models.FileField(upload_to='rrhh/empleados/', blank=True, null=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, blank=True, null=True,
                              limit_choices_to = {'active': True})


class Comunicacion(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Comunicacion'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return '{}: {}'.format(self.get_tipo_display(), self.texto)

    TIPO = (('movil', 'Celular'), ('tel', 'Teléfono'), ('wa', 'WhatsApp'), ('sms', 'Mensaje SMS'),
            ('email', 'Correo Electrónico'),
            ('face', 'Facebook'), ('git', 'GitHub'), ('gmail', 'Google+'),
            ('link', 'LinkedIn'), ('pint', 'Pinterest'), ('twitt', 'Twitter'),
            ('ytube', 'YouTube'))

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, blank=True, null=True,
                                 limit_choices_to={'active': True})
    tipo = models.CharField(max_length=5, choices=TIPO, default='movil')
    texto = models.CharField(max_length=150)


class Domicilio(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return self.domicilio

    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, default=1)
    domicilio = models.CharField(max_length=90, blank=False, null=False)
    localidad = models.CharField(max_length=40, blank=False, null=False)
    provincia = models.CharField(max_length=30, blank=False, null=False)
    cp = models.CharField(max_length=12, blank=False, null=False)
    pais = models.CharField(max_length=30, blank=False, null=False)


class Diccionario_ART(models.Model):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Diccionario ART'
        verbose_name_plural = 'Diccionarios ART'

    def __str__(self):
        return self.descripcion

    descripcion = models.CharField(max_length=80)
    diccionario = models.CharField(max_length=15)


class Denuncia_ART(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Denuncia ART'
        verbose_name_plural = 'Denuncias ART'
        ordering = ['fec_siniestro']

    def __str__(self):
        return str(self.siniestro)

    @property
    def dias_perdidos(self):
        if self.fec_alta_medica is None:
            return (timezone.now() - self.fec_siniestro).days
        else:
            return (self.fec_alta_medica - self.fec_siniestro).days

    ESTADO = [('P', 'Pendiente'), ('A', 'Aceptado'), ('R', 'Rechazado')]

    siniestro = models.IntegerField()
    empleado = models.ForeignKey(Empleado,
                                 on_delete=models.CASCADE, null=False,
                                 limit_choices_to = {'active': True})
    fec_siniestro = models.DateField('Fecha Siniestro', default=timezone.now, blank=True, null=True)
    fec_denuncia = models.DateField('Fecha Denuncia', default=timezone.now, blank=True, null=True)
    tipo_accidente = models.ForeignKey(Diccionario_ART, models.DO_NOTHING, null=True, blank=True,
                                       related_name='tipo_accidente_id',
                                       verbose_name='Tipo de Accidente',
                                       limit_choices_to = {'diccionario': 'tipoAccidente'})
    tipologia = models.ForeignKey(Diccionario_ART, models.DO_NOTHING, null=True, blank=True,
                                  related_name='tipologia_id',
                                  limit_choices_to = {'diccionario': 'tipologia'})
    zona_afectada = models.TextField('Zona Afectada', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO, default='P', blank=True, null=True)
    fec_alta_medica = models.DateField('Fecha Alta', blank=True, null=True)
    motivo_alta = models.ForeignKey(Diccionario_ART, models.DO_NOTHING, null=True, blank=True,
                                    related_name='motivo_alta_id',
                                    verbose_name='Motivo de Alta',
                                    limit_choices_to = {'diccionario': 'motivoAlta'})


# Mantenimiento
#         +-----> Activo
#         +-----> Documentacion

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class Mantenimiento(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return str(self.descripcion)

    ESTADO = [('A', 'Atención'), ('C', 'Cumple'), ('N', 'No Cumple')]

    # campos necesarios para utilizar ContentTypes
    content_type =   models.ForeignKey(ContentType, models.DO_NOTHING, limit_choices_to = {'app_label': 'rrhh'})
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')

    descripcion = models.CharField(max_length=60)
    estado = models.CharField(max_length=1, choices=ESTADO, default='C')
    proximo = models.DateField('Próxima Verificación', default=timezone.now, blank=True, null=True)


class Activo(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'
        ordering = ['tipo', 'identificacion']

    def __str__(self):
        return str(self.identificacion)

    TIPO = [('D', 'Depósito'), ('V', 'Vehículo')]

    tipo = models.CharField(max_length=1, choices=TIPO, default='D')
    identificacion = models.CharField(max_length=40)
    responsable = models.ForeignKey(Empleado, models.DO_NOTHING, null=True, blank=True,
                                    limit_choices_to = {'active': True})
    # campo necesario para utilizar ContentTypes asociado a la tabla Mantenimiento
    mantenimientos = GenericRelation(Mantenimiento)


class Documentacion(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Documentación'
        verbose_name_plural = 'Documentaciones'
        ordering = ['activo', 'descripcion']

    def __str__(self):
        return str(self.descripcion)

    @property
    def dias_vencido(self):
        if self.fecha_final is None:
            return 0
        return (timezone.now() - self.fecha_final).days

    activo = models.ForeignKey(Activo, models.DO_NOTHING, null=True, blank=True,
                               related_name = 'documentaciones',
                               limit_choices_to = {'active': True})
    descripcion = models.CharField(max_length=60)
    fecha_inicial = models.DateField('Fecha Inicial', default=timezone.now, blank=True, null=True)
    fecha_final = models.DateField('Fecha Final', default=timezone.now, blank=True, null=True)
    archivo = models.FileField(upload_to='rrhh/activos/', blank=True, null=True)
    # campo necesario para utilizar ContentTypes asociado a la tabla Mantenimiento
    mantenimientos = GenericRelation(Mantenimiento)


