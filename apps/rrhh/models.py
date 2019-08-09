from django.db import models

# Create your models here.
class Persona(models.Model):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return '{}, {}'.format(self.nombre, self.apellido)

    id = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    nombre = models.CharField(max_length=60, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=True, null=True)
    cuil = models.CharField(max_length=13, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    fec_nac = models.DateTimeField(blank=True, null=True)


TIPO = (('tel', 'Teléfono'), ('movil', 'Celular'), ('wa', 'WhatsApp'),
        ('email', 'Correo Electrónico'), ('face', 'Facebook'),
        ('twitt', 'Twitter'), ('link', 'LinkedIn'))


class Comunicacion(models.Model):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Comunicacion'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return '{}: {}'.format(self.get_tipo_display(), self.texto)

    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=5, choices=TIPO, default='movil')
    texto = models.CharField(max_length=150)


class Empleado(models.Model):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['persona__apellido', 'persona__nombre']

    def __str__(self):
        return '{}, {}'.format(self.persona.apellido, self.persona.nombre)

    id = models.IntegerField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False)
    legajo = models.IntegerField(blank=False, null=False)
    fec_ing = models.DateTimeField(blank=True, null=True)
    fec_egr = models.DateTimeField(blank=True, null=True)
    comunicaciones = models.ManyToManyField(Comunicacion, related_name='empleado_comunicaciones', blank=True)


class Domicilio(models.Model):
    class Meta:
        app_label = 'rrhh'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return self.domicilio

    id = models.IntegerField(primary_key=True)
    domicilio = models.CharField(max_length=90, blank=False, null=False)
    localidad = models.CharField(max_length=40, blank=False, null=False)
    provincia = models.CharField(max_length=30, blank=False, null=False)
    cp = models.CharField(max_length=12, blank=False, null=False)
    pais = models.CharField(max_length=30, blank=False, null=False)


# CREATE TABLE `Personal` (
# 	`Tel_Movil` DOUBLE,
# 	`Tel_Fijo` DOUBLE,
# 	`Cod_OS` DOUBLE DEFAULT 0,
# 	`Seg_Vida_Oblig` VARCHAR(255),
# 	`Cert_Seg_Vida_Oblig` VARCHAR(255),
# 	`Tarea a realizar` VARCHAR(255),
# 	`Fecha_Pre` TIMESTAMP,
# 	`Emp_Laboral` VARCHAR(255),
# 	`Res_Preoc` VARCHAR(255),
# 	`Fech_Period` TIMESTAMP