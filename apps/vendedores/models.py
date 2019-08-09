from django.db import models

from apps.comunes.models import Provincias, Zonas

# Create your models here.
class Vendedores(models.Model):
    class Meta:
        managed = False
        db_table = 'vendedor'
        app_label = 'firebird'
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.nombre

    idvendedor = models.IntegerField(primary_key=True)
    provincia = models.ForeignKey(Provincias, models.DO_NOTHING, db_column='idprovincias')
    zona = models.ForeignKey(Zonas, models.DO_NOTHING, db_column='idzona')
    nombre = models.CharField(max_length=60, blank=True, null=True)
    comentario = models.CharField(max_length=60, blank=True, null=True)
    tipcom = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    codpostal = models.CharField(max_length=12, blank=True, null=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)
    telefono1 = models.CharField(max_length=40, blank=True, null=True)
    # comvta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

