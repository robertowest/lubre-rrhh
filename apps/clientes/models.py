from django.db import models


class Actividades(models.Model):
    idactividad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        app_label = 'firebird'
        db_table = 'actividades'
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'


class Califica(models.Model):
    idcalifica = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        app_label = 'firebird'
        db_table = 'califica'


class Estadocliente(models.Model):
    idestadocliente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        app_label = 'firebird'
        db_table = 'estadocliente'


class Provincias(models.Model):
    idprovincias = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        app_label = 'firebird'
        db_table = 'provincia'


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    actividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='idactividad')
    califica = models.ForeignKey(Califica, models.DO_NOTHING, db_column='idcalifica')
    estadocliente = models.ForeignKey(Estadocliente, models.DO_NOTHING, db_column='idestadocliente')
    direc_d = models.CharField(max_length=60, blank=True, null=True)
    directivos = models.CharField(max_length=60, blank=True, null=True)
    telef_d = models.CharField(max_length=20, blank=True, null=True)
    email_d = models.CharField(max_length=90, blank=True, null=True)
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING, db_column='idprovincias')
    localidad = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.fantasia

    class Meta:
        managed = False
        app_label = 'firebird'
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

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
