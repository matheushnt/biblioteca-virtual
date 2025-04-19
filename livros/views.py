from django.shortcuts import render, get_object_or_404
from .models import Livro


def lista_livros(request):
    livros = Livro.objects.all()
    context = {
        'livros': livros,
    }
    return render(request, 'livros/lista.html', context)


def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    context = {
        'livro': livro
    }
    return render(request, 'livros/detalhes.html', context)
