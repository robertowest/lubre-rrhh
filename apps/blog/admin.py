from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'estado', 'created')
    list_filter = ("estado",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Post, PostAdmin)