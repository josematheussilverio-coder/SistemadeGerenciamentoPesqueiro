from django.contrib import admin
from .models import *


class ItemComandaInline(admin.TabularInline):
    model = ItemComanda
    extra = 1

class ComandaAdmin(admin.ModelAdmin):
    inlines = [ItemComandaInline]
    list_display = ('id', 'cliente', 'aberta', 'total')
    list_filter = ('aberta',)

    def total(self, obj):
        return f'R$ {obj.total:.2f}'
    total.short_description = 'Total da Comanda'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'tipo')
    list_filter = ('tipo',)

admin.site.register(Cliente)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Comanda, ComandaAdmin)
