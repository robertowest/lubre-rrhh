import datetime

from betterforms.multiform import MultiModelForm
from bootstrap_modal_forms.forms import BSModalForm
from django import forms

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

    def __init__(self, *args, **kwargs):
        super(EmpleadoFiltro, self).__init__(*args, **kwargs)
        self.fields['active'].initial = True

    nombre = forms.CharField(label='Nombre', max_length=60, required=False)
    apellido = forms.CharField(label='Apellido', max_length=60, required=False)

    # CHOICES = [(False, 'Todos'), (True, 'Activos')]
    # estado = forms.ChoiceField(label='Estado', initial=True, choices=CHOICES)


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
        widgets = {
            # 'zona_afectada': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        instance = super(DenunciaForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            # asignamos el empleado al registro actual
            # obtenemos el valor de empl_id pasado por la url
            empl_id = self.request.resolver_match.kwargs['empl_id']
            empleado = models.Empleado.objects.get(persona_id=empl_id)
            self.fields['empleado'].initial = empleado
        self.fields['empleado'].disabled = True

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
        if instance == None:
            # asignamos el activo al registro actual
            # obtenemos el valor de activo_id pasado por la url
            activo_id = self.request.resolver_match.kwargs['activo_id']
            activo_obj = models.Activo.objects.get(id=activo_id)
            self.fields['activo'].initial = activo_obj
        # self.fields['activo'].disabled = True

    def get_tipo_activo(self):
        activo_id = self.request.resolver_match.kwargs['activo_id']
        activo = models.Activo.objects.get(id=activo_id)
        return activo.tipo


class MantenimientoFormCheck(MyModelForm):
    class Meta:
        model = models.Mantenimiento
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by',)

    def __init__(self, *args, **kwargs):
        super(MantenimientoFormCheck, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['activo'].widget.attrs['readonly'] = True
            self.fields['descripcion'].widget.attrs['readonly'] = True


class VacacionesForm(MyBSModelForm):
    class Meta:
        model = models.Vacaciones
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by', )
        widgets = {
            'fec_inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fec_fin': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'observacion': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        instance = super(VacacionesForm, self).__init__(*args, **kwargs)

        if not self.instance.id:
            # asignamos el empleado al registro actual
            # obtenemos el valor de empl_id pasado por la url
            empl_id = self.request.resolver_match.kwargs['empl_id']
            empleado = models.Empleado.objects.get(persona_id=empl_id)
            self.fields['empleado'].initial = empleado
            self.fields["fec_solicitud"].initial = datetime.date.today()
            self.fields["fec_inicio"].initial = datetime.date.today()
            self.fields["fec_fin"].initial = datetime.date.today()
            self.fields["periodo"].initial = self.request.resolver_match.kwargs['anio']

        self.fields['empleado'].disabled = True
        self.fields["fec_solicitud"].disabled = True
        self.fields['estado'].disabled = True

    def clean(self):
        cleaned_data = super(VacacionesForm, self).clean()
        fec_inicio = cleaned_data.get("fec_inicio")
        fec_fin = cleaned_data.get("fec_fin")

        if cleaned_data.get("periodo") == datetime.date.today().year:
            if fec_inicio <= datetime.date.today():
                raise forms.ValidationError("La fecha inicial debe ser posterior al día de hoy.")
            elif fec_inicio > fec_fin:
                raise forms.ValidationError("La fecha de inicio no puede ser posterior a la de finalización.")

        return cleaned_data


class VacacionesFiltro(MyModelForm):
    # empleado = forms.ChoiceField(models.Empleado)
    periodo = forms.IntegerField(label='Período', required=False)

    class Meta:
        model = models.Vacaciones
        fields = ('empleado', 'periodo', 'estado')

    def __init__(self, *args, **kwargs):
        super(VacacionesFiltro, self).__init__(*args, **kwargs)
        self.fields['empleado'].required = False
        self.fields['periodo'].initial = datetime.date.today().year
        self.fields['estado'].initial = None
        self.fields['estado'].required = False

        # agregamos un campo que no existe en el modelo
        CHOICES = ((None, 'Todos'),
                   (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
                   (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
                   (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'))
        self.fields['mes'] = forms.ChoiceField(choices=CHOICES)

        # obtenemos el mes siguiente de la fecha actual
        # (nos vamos al primer día del mes y le sumamos 32 días para llegar al próximo mes)
        mes = ((datetime.date.today().replace(day=1)) + datetime.timedelta(days=32)).month
        self.fields['mes'].initial = mes
