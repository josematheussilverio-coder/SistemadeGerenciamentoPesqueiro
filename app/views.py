from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ClienteForm, ProdutoForm, ItemComandaForm


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
    template_name = 'cliente.html'
    context_object_name = 'clientes'

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto.html'
    context_object_name = 'produtos'   

class ComandaListView(ListView):
    model = Comanda
    template_name = 'comanda.html'
    context_object_name = 'comandas'
    ordering = ['-data_criacao'] 
        
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    extra_context = {'titulo': 'Novo Cliente'}

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    extra_context = {'titulo': 'Editar Cliente'}

class ComandaCreateView(CreateView):
    model = Comanda
    fields = ['cliente']
    template_name = 'comanda_form.html'
    success_url = reverse_lazy('comanda_list')

class ComandaDetailView(DetailView):
    model = Comanda
    template_name = 'comanda_detail.html'

class AdicionarItemView(CreateView):
    model = ItemComanda
    form_class = ItemComandaForm
    template_name = 'item_comanda_form.html'

    def form_valid(self, form):
        comanda_id = self.kwargs['pk']
        comanda = get_object_or_404(Comanda, id=comanda_id)
        
        form.instance.comanda = comanda
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('comanda_detail', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comanda'] = get_object_or_404(Comanda, pk=self.kwargs['pk'])
        return context

class ComandaDeleteView(DeleteView):
    model = Comanda
    template_name = 'comanda_delete.html'
    success_url = reverse_lazy('comanda_list')
