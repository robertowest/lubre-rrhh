from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def home(request):
    # template = loader.get_template('base_b3.html')
    # return HttpResponse(template.render())
    # return render(request, 'home.html')
    return HttpResponseRedirect('/rrhh/')

def demo(request):
    return render(request, 'demo.html')

def modal(request):
    return render(request, 'modal.html')