from django.shortcuts import render
from django.views import generic

from . import models

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')


class PostList(generic.ListView):
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(status=1).order_by('-created')

    model = models.Post
    template_name = 'blog/index.html'
    paginate_by = 25


class PostDetail(generic.DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'