from django import forms

from .models import Clientes
from .models import Actividades, Provincias

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Clientes
        # fields = ('nombre',)
        fields = ('__all__')
        exclude = ('idcliente',)


    nombre = forms.CharField(label='Nombre', max_length=60)
    fantasia = forms.CharField(label='Razón Social', max_length=60)
    direc_d = forms.CharField(label='Domicilio', max_length=60)
    telef_d = forms.CharField(label='Teléfono', max_length=20)
    email_d = forms.CharField(label='Correo Electrónico', max_length=90)
    actividad = forms.ModelChoiceField(queryset=Actividades.objects.all().order_by('descripcion'))
    provincia = forms.ModelChoiceField(queryset=Provincias.objects.all().order_by('nombre'))

    # form = YourForm(initial={'field1': instance_of_mymodel})
    # field1 = forms.ModelChoiceField(queryset=..., initial=0)

    # actividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='idactividad')
    # califica = models.ForeignKey(Califica, models.DO_NOTHING, db_column='idcalifica')
    # estadocliente = models.ForeignKey('Estadocliente', models.DO_NOTHING, db_column='idestadocliente')
    # directivos = models.CharField(max_length=60, blank=True, null=True)
    # idprovincias = models.CharField(max_length=15, blank=True, null=True)
    # localidad = models.CharField(max_length=60, blank=True, null=True)
    # direccion = models.CharField(max_length=60, blank=True, null=True)

