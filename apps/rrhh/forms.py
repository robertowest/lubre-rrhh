from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.contrib.contenttypes.models import ContentType

from betterforms.multiform import MultiModelForm

from . import models


# agregamos la clase form-control a todos los campos
class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PersonaForm(MyModelForm):
    class Meta:
        model = models.Persona
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
        model = models.Empleado
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
        model = models.Empleado
        fields = ('nombre', 'apellido', 'active')
        labels = {'active': 'Estado'}
        widgets = {
            'active': forms.Select(choices=((False, 'Todos'), (True, 'Activos')))
        }

    nombre = forms.CharField(label='Nombre', max_length=60, required=False)
    apellido = forms.CharField(label='Apellido', max_length=60, required=False)


class ComunicacionForm(MyModelForm):
    class Meta:
        model = models.Comunicacion
        fields = ['tipo', 'texto']
        labels = {
            'texto': 'Contenido',
        }


# agregamos la clase form-control a todos los campos
class MyBSModelForm(BSModalForm):
    def __init__(self, *args, **kwargs):
        super(MyBSModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DenunciaForm(MyBSModelForm):
    class Meta:
        model = models.Denuncia_ART
        fields = ['siniestro', 'empleado', 'fec_siniestro', 'fec_denuncia',
                  'tipo_accidente', 'tipologia', 'zona_afectada', 'estado',
                    'fec_alta_medica', 'motivo_alta']
        # fields = ('__all__')
        # exclude = ('active', 'created', 'created_by', 'modified', 'modified_by')

# -----------------------------------------------------------------------------
# formularios de asignaciones (activos y mantenimientos

class ActivoForm(MyBSModelForm):
    class Meta:
        model = models.Activo
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by', )

    def __init__(self, *args, **kwargs):
        instance = super(ActivoForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            # asignamos el empleado al registro actual
            # obtenemos el valor de empl_id pasado por la url
            empl_id = self.request.resolver_match.kwargs['empl_id']
            empleado = models.Empleado.objects.get(persona_id=empl_id)
            self.fields['responsable'].initial = empleado
        self.fields['responsable'].disabled = True

    # def get_form_kwargs(self):
    #     # agregamos el uausio logeado
    #     kwargs = {'user' : self.request.user , }
    #     return kwargs

    # def get_form_kwargs(self):
    #     kwargs = super(VenueCreateView, self).get_form_kwargs()
    #     kwargs.update({'user' : self.request.user})
    #     return kwargs

class MantenimientoForm(MyBSModelForm):
    class Meta:
        model = models.Mantenimiento
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by', )

    def __init__(self, *args, **kwargs):
        instance = super(MantenimientoForm, self).__init__(*args, **kwargs)
        if not instance:
            # asignamos el activo al registro actual
            # obtenemos el valor de activo_id pasado por la url
            activo_id = self.request.resolver_match.kwargs['activo_id']
            activo = models.Activo.objects.get(id=activo_id)
            self.fields['activo'].initial = activo
        self.fields['activo'].disabled = True

    def get_tipo_activo(self):
        activo_id = self.request.resolver_match.kwargs['activo_id']
        activo = models.Activo.objects.get(id=activo_id)
        return activo.tipo