from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView, DetailView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('comandas/', ComandaListView.as_view(), name='comanda_list'),
    path('cliente/novo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name= 'cliente_update'),
    path('comanda/nova/', ComandaCreateView.as_view(), name='comanda_create'),
    path('comanda/<int:pk>/', ComandaDetailView.as_view(), name='comanda_detail'),
    path('comanda/<int:pk>/adicionar-item/', AdicionarItemView.as_view(), name='adicionar_item'),
    path('comanda/<int:pk>/excluir/', ComandaDeleteView.as_view(), name='comanda_delete'),
    path('produto/novo/', ProdutoCreateView.as_view(), name='produto_create' ),
    path('produto/excluir/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),
    path('item/excluir/<int:pk>/', ItemComandaDeleteView.as_view(), name='item_comanda_delete'),
]


