from django.db import models

# Create your models here.
class Provincias(models.Model):
    class Meta:
        managed = False
        db_table = 'provincia'
        app_label = 'firebird'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre

    idprovincias = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    dgi = models.IntegerField(blank=True, null=True)
    declara = models.CharField(max_length=1, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)


class Zonas(models.Model):
    class Meta:
        managed = False
        db_table = 'zonas'
        app_label = 'firebird'
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return self.descripcion

    idzona = models.IntegerField(primary_key=True)
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING, db_column='idprovincias')
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    fechaalta = models.DateTimeField(blank=True, null=True)
    datospc = models.CharField(max_length=60, blank=True, null=True)
    idopera = models.IntegerField(blank=True, null=True)

