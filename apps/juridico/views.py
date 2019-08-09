from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import DeudaView
from .forms import DeudaFiltro

class Listado(ListView, FormView):
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            if form.cleaned_data['vendedor']:
                self.object_list = self.object_list.filter(vendedor=form.cleaned_data['vendedor'])

        return self.render_to_response(self.get_context_data(object_list=self.object_list.order_by('-dias'), form=form))

    def get_queryset(self):
        queryset = super().get_queryset()
        # return queryset.filter(vendedor=0).order_by('fecha')
        return queryset.filter(vendedor=0).order_by('-dias')

    model = DeudaView   # .objects.filter(vendedor=0).order_by('fecha')
    form_class = DeudaFiltro
    template_name = 'deuda/listado.html'
    success_url = reverse_lazy('juridico:show')
    paginate_by = 25
