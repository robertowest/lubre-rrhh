from apps.comunes.models import AudtoriaMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.deconstruct import deconstructible

import os

class Persona(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.apellido)

    SEXO = (('M', 'Masculino'), ('F', 'Femenino'))

    apellido = models.CharField(max_length=30, blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=True, null=True)
    cuil = models.CharField(max_length=13, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    fec_nac = models.DateField(blank=True, null=True)


class Comunicacion(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Comunicacion'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return '{}: {}'.format(self.get_tipo_display(), self.texto)

    TIPO = (('movil', 'Celular'), ('tel', 'Teléfono'), ('wa', 'WhatsApp'), ('sms', 'Mensaje SMS'),
            ('email', 'Correo Electrónico'),
            ('face', 'Facebook'), ('git', 'GitHub'), ('google', 'Google+'),
            ('link', 'LinkedIn'), ('pinter', 'Pinterest'), ('twitt', 'Twitter'))

    tipo = models.CharField(max_length=5, choices=TIPO, default='movil')
    texto = models.CharField(max_length=150)


class Empleado(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['persona__apellido', 'persona__nombre']

    def __str__(self):
        return '{}, {}'.format(self.persona.apellido, self.persona.nombre)

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('rrhh:empl_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('rrhh:empl_edit', args=(self.pk,))

    # def get_delete_url(self):
    #     return reverse('rrhh:empl_delete', args=(self.pk,))

    def get_success_url(self):
        return reverse('rrhh:empl_show')

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    legajo = models.IntegerField(blank=False, null=False)
    fec_ing = models.DateField(blank=True, null=True)
    fec_egr = models.DateField(blank=True, null=True)
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='empleado_comunicaciones', blank=True)
    imagen = models.FileField(upload_to='rrhh/empleados/', blank=True, null=True)


class Domicilio(AudtoriaMixin):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return self.domicilio

    domicilio = models.CharField(max_length=90, blank=False, null=False)
    localidad = models.CharField(max_length=40, blank=False, null=False)
    provincia = models.CharField(max_length=30, blank=False, null=False)
    cp = models.CharField(max_length=12, blank=False, null=False)
    pais = models.CharField(max_length=30, blank=False, null=False)
