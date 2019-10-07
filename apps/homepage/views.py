from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def home(request):
    # template = loader.get_template('base_b3.html')
    # return HttpResponse(template.render())
    # return render(request, 'home.html')
    # return HttpResponseRedirect('/rrhh/')

    if request.user.is_anonymous == False:
        # dirige la ejecución a la aplicación del grupo proncipal
        groups = request.user.groups.filter(user=request.user)
        if groups:
            group = groups[0]
            if group.name == "Empleados":
                return HttpResponseRedirect(reverse('empleados:index'))
            elif group.name == "RRHH":
                return HttpResponseRedirect(reverse('rrhh:home'))
            # elif group.name=="admin":
            #     return HttpResponseRedirect(reverse('adm'))
    # por defecto
    return HttpResponseRedirect('/empleados/')



def example(request):
    return render(request, 'homepage.html')

def demo(request):
    return render(request, 'demo.html')

def modal(request):
    return render(request, 'modal.html')