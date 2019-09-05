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


class MantenimientoForm(MyModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs:
            self.fields['content_type'].queryset = \
                ContentType.objects.filter(models.Q(model='activo') | models.Q(model='documentacion'))


class DocumentoForm(MyBSModelForm):
    # responsable = forms.ModelChoiceField(label='Empleado',
    #                                      queryset=Empleado.objects.all(),
    #                                      # to_field_name="name",
    #                                      widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = models.Documentacion
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by', )

    def __init__(self, *args, **kwargs):
        instance = super(DocumentoForm, self).__init__(*args, **kwargs)
        if not self.instance.responsable:
            # obtenemos el valor de empl_id pasado por la url
            empl_id = self.request.resolver_match.kwargs['empl_id']
            empleado = models.Empleado.objects.get(persona_id=empl_id)
            self.fields['responsable'].initial = empleado
        self.fields['responsable'].disabled = True

    # def save(self, commit=False):
    #     # import pdb; pdb.set_trace()
    #     instance = super(DocumentoForm, self).save(commit=False)
    #     if not self.instance.responsable:
    #         empl_id = self.request.resolver_match.kwargs['empl_id']
    #         empleado = models.Empleado.objects.get(persona_id=empl_id)
    #         instance.responsable = empleado
    #         if commit:
    #             instance.save()
    #     return instance


class ActivoForm(MyBSModelForm):
    class Meta:
        model = models.Activo
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by', )
