from django.db import models

from apps.comunes.models import Provincias

class Canales(models.Model):
    class Meta:
        # app_label = 'firebird'
        db_table = 'canales'
        managed = False
        verbose_name = 'Canal'
        verbose_name_plural = 'Canales'

    def __str__(self):
        return self.descripcion

    idcanales = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)


class Actividades(models.Model):
    class Meta:
        # app_label = 'firebird'
        db_table = 'actividades'
        managed = False
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return self.descripcion

    idactividad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idcanales = models.ForeignKey('Canales', models.DO_NOTHING, db_column='idcanales')
    secretaria = models.CharField(max_length=1, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)


class Califica(models.Model):
    class Meta:
        # app_label = 'firebird'
        db_table = 'califica'
        managed = False

    def __str__(self):
        return self.descripcion

    idcalifica = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)


class Estadocliente(models.Model):
    class Meta:
        # app_label = 'firebird'
        db_table = 'estadocliente'
        managed = False

    def __str__(self):
        return self.descripcion

    idestadocliente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)


class Clientes(models.Model):
    class Meta:
        # app_label = 'firebird'
        db_table = 'clientes'
        managed = False
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.fantasia

    def get_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:
            fname = f.name
            try:
                value = getattr(self, fname)
            except:
                value = None

            # solo muestra campos con valores y que no sean campos especiales
            if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete'):
                fields.append({'name':fname, 'value':value,})

        return fields

    idcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    # models.DO_NOTHING
    actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE, db_column='idactividad', blank=True)
    califica = models.ForeignKey(Califica, on_delete=models.CASCADE, db_column='idcalifica', blank=True)
    estadocliente = models.ForeignKey(Estadocliente, on_delete=models.CASCADE, db_column='idestadocliente', blank=True)
    direc_d = models.CharField(max_length=60, blank=True, null=True)
    directivos = models.CharField(max_length=60, blank=True, null=True)
    telef_d = models.CharField(max_length=20, blank=True, null=True)
    email_d = models.CharField(max_length=90, blank=True, null=True)
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE, db_column='idprovincias')
    localidad = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)


