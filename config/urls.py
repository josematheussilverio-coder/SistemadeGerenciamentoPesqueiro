from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('comandas/', ComandaListView.as_view(), name='comanda_list'),
]


