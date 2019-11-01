from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from apps.rrhh.models import Empleado

def a_donde_voy(request):
    # url = reverse('homepage:index')

    if request.user.is_anonymous:
        url = reverse('usuarios:login')

    else:
        # obtenemos todos los grupos del usuario
        groups = request.user.groups.filter(user=request.user)

        if groups:
            group = groups[0]   # seleccionamos el grupo principal

            if group.name == "Empleados":
                # usuario = request.user
                # empleado = Empleado.objects.get(user_id=usuario.id)
                # url = reverse('rrhh:empl_detail', kwargs={'pk': empleado.persona.id})
                url = reverse('rrhh:empl_index')

            elif group.name == "RRHH":
                url = reverse('rrhh:home')

            else:
                url = reverse('rrhh:empl_index')

    return url


def index(request):
    return render(request, 'homepage.html')


def home(request):
    url = a_donde_voy(request)
    return HttpResponseRedirect(url)


def example(request):
    return render(request, 'example.html')


def demo(request):
    return render(request, 'demo.html')


def modal(request):
    return render(request, 'modal.html')


def prueba(request):
    crearCVS()
    return HttpResponse('Prueba ejecutada')


import csv

def crearCVS():
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def crearPDF(self):
    # Create a file-like buffer to receive PDF data.
    buffer = io.StringIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
