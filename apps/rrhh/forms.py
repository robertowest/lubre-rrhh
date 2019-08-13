from django import forms

from betterforms.multiform import MultiModelForm

from .models import Empleado, Persona

class PersonaModelForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni', 'cuil', 'sexo', 'fec_nac']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
        }


class EmpleadoModelForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['fec_ing', 'fec_egr'] # No agregar el campo 'persona'


class EmpleadoPersonaModelForm(MultiModelForm):
    def save(self, commit=True):
        objects = super().save(commit=False)
        if commit:
            persona = objects['persona']
            persona.save()
            empleado = objects['empleado']
            empleado.persona = persona
            empleado.save()
        return objects

    form_classes = {
        'persona': PersonaModelForm,
        'empleado': EmpleadoModelForm,
    }

    # nombre = forms.CharField(max_length=60, required=True)
    # apellido = forms.CharField(max_length=60, required=True)
    # dni = forms.CharField(label='DNI', max_length=8)
    # cuil = forms.CharField(label='CUIL', max_length=8)
    # sexo = forms.ModelChoiceField(queryset=models.SEXO, required=False)
    # fec_nac = models.DateTimeField(blank=True, null=True)

