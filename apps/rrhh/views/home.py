from bootstrap_modal_forms.generic import BSModalReadView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone

from apps.blog.models import Post

from apps.rrhh import models


def home(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    # vencimientos = Documentacion.objects.all()  # filter('dias_vencido': 0)

    # Model.objects.filter(Q(x=1) & Q(y=2))
    # vencimientos = Documentacion.objects.filter(Q(dias_vencido='0'))
    mantenimientos = models.Mantenimiento.objects.filter(proximo__lt=timezone.now())
    vencimientos = models.Mantenimiento.objects.filter(fecha_final__lt=timezone.now())
    # noticias = Post.objects.filter(estado=1).order_by('-created')
    noticias = Post.objects.all().order_by('-created')
    return render(request, 'rrhh/home.html', {'mantenimientos': mantenimientos,
                                              'noticias': noticias,
                                              'vencimientos': vencimientos})


class PostReadView(LoginRequiredMixin, BSModalReadView):
    model = Post
    template_name = 'comunes/read-modal.html'