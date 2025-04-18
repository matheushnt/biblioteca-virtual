from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'autor',
        'data_publicacao',
        'isbn',
    ]
    list_display_links = [
        'titulo',
        'isbn',
    ]
