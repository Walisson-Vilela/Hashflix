from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)


# Criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='tumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo   


# Criar os episodios


