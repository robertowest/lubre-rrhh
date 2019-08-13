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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['apellido'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['dni'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['cuil'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['sexo'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['fec_nac'].widget.attrs.update({'class': 'form-control'})
    #
    # fec_nac = forms.CharField(label='Fecha Nacimiento', )


class EmpleadoModelForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['fec_ing', 'fec_egr'] # No agregar el campo 'persona'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['fec_ing'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['fec_egr'].widget.attrs.update({'class': 'form-control'})


class EmpleadoPersonaModelForm(MultiModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # for field in iter(self.fields):
    #     #     if self.fields[field].widget.__class__.__name__ \
    #     #             in ('AdminTextInputWidget', 'Textarea', 'NumberInput', 'AdminURLFieldWidget', 'Select'):
    #     #         self.fields[field].widget.attrs.update({'class': 'form-control'})
    #
    #     # for field in self.fields:
    #     #     self.fields[field].widget.attrs.update({
    #     #         'class': 'form-control'
    #     #     })
    #
    #     for field in iter(self.fields):
    #         #get current classes from Meta
    #         classes = self.fields[field].widget.attrs.get("class")
    #         if classes is not None:
    #             classes += " form-control"
    #         else:
    #             classes = "form-control"
    #         self.fields[field].widget.attrs.update({'class': classes})

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         field.wiget.attrs['class'] = 'form-control'


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

