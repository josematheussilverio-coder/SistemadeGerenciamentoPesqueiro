from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django.views.generic import ListView


class IndexView(View):
    def get(self, request):
        clientes = Cliente.objects.all()
        produtos = Produto.objects.all()
        comandas_abertas = Comanda.objects.filter(aberta=True)
        context = {
            'clientes': clientes,
            'produtos': produtos,
            'comandas_abertas': comandas_abertas,
        }
        return render(request, 'index.html', context)
    


class ClienteListView(ListView):
    model = Cliente
    template_name = 'app/cliente_list.html'
    context_object_name = 'clientes'

class ProdutoListView(ListView):
    model = Produto
    template_name = 'app/produto_list.html'
    context_object_name = 'produtos'   

class ComandaListView(ListView):
    model = Comanda
    template_name = 'app/comanda_list.html'
    context_object_name = 'comandas'
    ordering = ['-data_criacao'] 
        
