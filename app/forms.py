from django import forms
from .models import Cliente, Produto, Comanda, ItemComanda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João da Silva'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) 99999-9999'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'tipo', 'estoque']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ItemComandaForm(forms.ModelForm):
    class Meta:
        model = ItemComanda
        fields = ['produto', 'quantidade']
        widgets ={
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }