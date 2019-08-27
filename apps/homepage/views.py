from django.shortcuts import render

# Create your views here.
def home(request):
    # template = loader.get_template('base_b3.html')
    # return HttpResponse(template.render())
    return render(request, 'home.html')

def demo(request):
    return render(request, 'demo.html')