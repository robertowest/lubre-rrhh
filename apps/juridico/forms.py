from django import forms

from apps.vendedores.models import Vendedores

class DeudaFiltro(forms.ModelForm):
    class Meta:
        model = Vendedores
        fields = ('vendedor',)

    vendedor = forms.ModelChoiceField(label='Comercial',
                                      queryset=Vendedores.objects.all().order_by('nombre'),
                                      required=False)
