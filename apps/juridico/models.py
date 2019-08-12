from django.db import models

from apps.comerciales.models import Comercial
from apps.clientes.models import Clientes

# Create your models here.
class DeudaView(models.Model):
    class Meta:
        app_label = 'firebird'
        default_permissions = ('view')
        db_table = 'deuda_cliente_vendedor_v'
        managed = False
        verbose_name = 'Deuda'
        verbose_name_plural = 'Deudas'

    def __str__(self):
        return self.comprobante

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

    vendedor = models.ForeignKey(Comercial, models.DO_NOTHING, db_column='idvendedor')
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente')
    comprobante = models.CharField(max_length=20, blank=True, null=True)
    idenc_mov = models.IntegerField(primary_key=True)
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)
