from django.urls import path
from . import views

app_name = 'livros'
urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('livros/<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('livros/novo/', views.criar_livro, name='criar_livro'),
]
