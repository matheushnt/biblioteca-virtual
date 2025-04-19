from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm


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


def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.autor = request.user
            livro.save()
            return redirect('livros:lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/form.html', {'form': form})
