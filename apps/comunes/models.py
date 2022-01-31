from datetime import datetime
from django.db import models

def get_current_user():
    username = None
    # from django.http import request
    # if request.user.is_authenticated():
    #     username = current_user()
    # return username
    return 'admin'

class AuditoriaMixin(models.Model):
    class Meta:
        abstract = True

    def get_fields(self):
        """Devuelve una lista con todos los nombres de campo de la entidad."""
        fields = []

        # descarta los campos especiales y los campos sin valor
        descarte = ('id', 'active',
                    'created', 'created_by', 'modified', 'modified_by',
                    'status', 'workshop', 'user', 'complete')

        for f in self._meta.fields:
            fname = f.name
            try:
                value = getattr(self, fname)
                if len(f.flatchoices) > 0:
                    value = dict(f.flatchoices).get(value)

            except:
                value = None
            if f.editable and value and f.name not in descarte:
                fields.append({'name': f.verbose_name, 'value': value, 'type': f.get_internal_type()})
        return fields

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self):
        super(AuditoriaMixin, self).delete()

    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        if not self.pk:
            self.created_by = get_current_user()
        else:
            self.modified_by = get_current_user()
        # if not self.created_by:
        #     self.created_by = get_current_user()
        # self.modified_by = get_current_user()
        super(AuditoriaMixin, self).save(*args, **kwargs)

    active = models.BooleanField('Activo', default=True)
    created = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True, blank=True)
    created_by = models.CharField('Creado por', max_length=15, editable=False, null=True, blank=True)
    modified = models.DateTimeField('Modificado', auto_now=True, editable=False, null=True, blank=True)
    modified_by = models.CharField('Modif. por', max_length=15, editable=False, null=True, blank=True)

# Create your models here.
class Provincias(models.Model):
    class Meta:
        app_label = 'clientes'
        db_table = 'provincia'
        managed = False
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
        app_label = 'clientes'
        db_table = 'zonas'
        managed = False
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
