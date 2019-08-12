from django import forms

from apps.comerciales.models import Comercial

class DeudaFiltro(forms.ModelForm):
    class Meta:
        model = Comercial
        fields = ('vendedor',)

    vendedor = forms.ModelChoiceField(label='Comercial',
                                      queryset=Comercial.objects.all().order_by('nombre'),
                                      required=False)
