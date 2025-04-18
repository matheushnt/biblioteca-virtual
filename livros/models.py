from django.db import models
from django.contrib.auth.models import User


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo
