from django import forms

from .models import Clientes
from .models import Actividades, Califica, Estadocliente, Provincias

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Clientes
        # fields = ('nombre',)
        fields = ('__all__')
        exclude = ('idcliente',)


    nombre = forms.CharField(label='Razón Social', max_length=60, required=False)
    fantasia = forms.CharField(label='Fantasía', max_length=60, required=False)
    direc_d = forms.CharField(label='Domicilio', max_length=60, required=False)
    telef_d = forms.CharField(label='Teléfono', max_length=20, required=False)
    email_d = forms.CharField(label='Correo Electrónico', max_length=90, required=False)
    actividad = forms.ModelChoiceField(queryset=Actividades.objects.all().order_by('descripcion'), required=False)
    provincia = forms.ModelChoiceField(queryset=Provincias.objects.all().order_by('nombre'), required=False)


class ClienteFiltro(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('nombre','actividad', 'califica', 'estadocliente')

    nombre = forms.CharField(label='Fantasía / Razón Social', max_length=60, required=False)
    califica = forms.ModelChoiceField(label='Calificación',
                                      queryset=Califica.objects.all().order_by('descripcion'),
                                      required=False)
    estadocliente = forms.ModelChoiceField(label='Estado',
                                           queryset=Estadocliente.objects.all().order_by('descripcion'),
                                           required=False)
