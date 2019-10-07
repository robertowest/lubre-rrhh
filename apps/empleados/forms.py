import datetime

from django import forms

from apps.rrhh.forms import MyBSModelForm
from apps.rrhh import models


class VacacionesForm(MyBSModelForm):
    class Meta:
        model = models.Vacaciones
        fields = ('__all__')
        exclude = ('active', 'created', 'created_by', 'modified', 'modified_by', )
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 4}),
        }
        fec_inicial = forms.DateTimeField(
            input_formats=['%d/%m/%Y'],
            widget=forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        )

    def __init__(self, *args, **kwargs):
        instance = super(VacacionesForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            # asignamos el empleado al registro actual
            # obtenemos el valor de empl_id pasado por la url
            empl_id = self.request.resolver_match.kwargs['empl_id']
            empleado = models.Empleado.objects.get(persona_id=empl_id)
            self.fields['empleado'].initial = empleado
        self.fields['empleado'].disabled = True
        self.fields["fec_solicitud"].initial = datetime.date.today()
        self.fields["fec_solicitud"].disabled = True
        self.fields['estado'].disabled = True
