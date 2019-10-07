import datetime

from django import forms
from datetimepicker.widgets import DateTimePicker

from apps.rrhh.forms import MyBSModelForm
from apps.rrhh import models


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

        self.fields['empleado'].disabled = True
        self.fields["fec_solicitud"].disabled = True
        self.fields['estado'].disabled = True
