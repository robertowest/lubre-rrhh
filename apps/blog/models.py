from django.db import models
from django.contrib.auth.models import User
from apps.comunes.models import AuditoriaMixin

class Post(AuditoriaMixin):
    ESTADO = ((0, 'Borrador'), (1, 'Publicado'))

    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    contenido = models.TextField()
    estado = models.IntegerField(choices=ESTADO, default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.titulo
