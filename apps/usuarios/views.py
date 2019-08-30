from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'usuario/registro.html', {'form': form})


@login_required(login_url='/usuarios/inicio/')
def profile(request):
    return render(request, 'usuario/perfil.html')


@login_required
def index(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "RRHH":
        return HttpResponseRedirect(reverse('rrhh:home'))
    # elif group.name=="admin":
    #     return HttpResponseRedirect(reverse('adm'))
    return redirect('/')
