from django.shortcuts import render
from .models import Livro


def lista_livros(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros,
    }
    return render(request, 'livros/lista.html', context)
