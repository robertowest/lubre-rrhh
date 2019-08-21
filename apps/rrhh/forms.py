from bootstrap_modal_forms.forms import BSModalForm
from django import forms

from betterforms.multiform import MultiModelForm

from .models import Comunicacion, Denuncia_ART, Empleado, Persona

# agregamos la clase form-control a todos los campos
class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PersonaForm(MyModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'dni', 'cuil', 'sexo', 'fec_nac']
        # fields = ('__all__')
        # exclude = ('id',)
        labels = {
            'dni': 'DNI',
            'cuil': 'CUIL',
            'fec_nac': 'Fecha Nacimiento',
        }


class EmpleadoForm(MyModelForm):
    class Meta:
        model = Empleado
        fields = ['fec_ing', 'fec_egr', 'imagen'] # No agregar el campo 'persona'
        labels = {
            'fec_ing': 'Fecha Ingreso',
            'fec_egr': 'Fecha Egreso',
        }


class EmpleadoMultiForm(MultiModelForm):
    def save(self, commit=True):
        objects = super().save(commit=False)
        if commit:
            persona = objects['persona']
            persona.save()
            empleado = objects['empleado']
            empleado.persona = persona
            empleado.legajo = str(persona.id).zfill(4)
            empleado.save()
        return objects

    form_classes = {
        'persona': PersonaForm,
        'empleado': EmpleadoForm,
    }


class EmpleadoFiltro(MyModelForm):
    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido', 'active')
        labels = {'active': 'Estado'}
        widgets = {
            'active': forms.Select(choices=((False, 'Todos'), (True, 'Activos')))
        }

    nombre = forms.CharField(label='Nombre', max_length=60, required=False)
    apellido = forms.CharField(label='Apellido', max_length=60, required=False)


class ComunicacionForm(MyModelForm):
    class Meta:
        model = Comunicacion
        fields = ['tipo', 'texto']
        labels = {
            'texto': 'Contenido',
        }


# agregamos la clase form-control a todos los campos
class MyBSModelForm(BSModalForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DenunciaForm(MyBSModelForm):
    class Meta:
        model = Denuncia_ART
        fields = ['siniestro', 'empleado', 'fec_siniestro', 'fec_denuncia',
                  'tipo_accidente', 'tipologia', 'zona_afectada', 'estado',
                    'fec_alta_medica', 'motivo_alta']
        # fields = ('__all__')
        # exclude = ('active', 'created', 'created_by', 'modified', 'modified_by')



