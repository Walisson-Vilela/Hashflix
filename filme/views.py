from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_list -> Lista de itens de modelo

# View para lista de detalhes
class Detalhesfilmes(DetailView):
    template_name = "detalhesfilmes.html"
    model = Filme
    # object -> 1 item do nosso modelo