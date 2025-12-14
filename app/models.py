from django.db import models
from django.core.exceptions import ValidationError


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Cliente")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    telefone = models.CharField(max_length=20, verbose_name="Telefone", blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Produto(models.Model):

    TIPOS_CHOICES = [
        ('PR', 'Bebida/Comida'),
        ('PE', 'Pesca esportiva'),
        ('PK', 'Pesca por quilo'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Unitário/kg")
    tipo = models.CharField(max_length=2, choices=TIPOS_CHOICES, verbose_name="Tipo de Produto")
    estoque = models.IntegerField(default=0, verbose_name="Estoque Disponível")


    def __str__(self):
        return f'{self.nome} - R$ {self.preco} - Quantidade em estoque: {self.estoque}'
        
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Comanda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente")
    aberta = models.BooleanField(default=True, verbose_name="Comanda Aberta?")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Abertura")

    @property
    def total(self):
        itens = self.itemcomanda_set.all()
        total = sum([item.subtotal for item in itens])
        return total

    def __str__(self):
        status = "Aberta" if self.aberta else "Fechada"
        return f'Comanda {self.id} - {self.cliente.nome} - {status}'
    
    class Meta:
        verbose_name = "Comanda"
        verbose_name_plural = "Comandas"

class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, verbose_name="Comanda")
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, verbose_name="Produto")
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=1, verbose_name="Quantidade / kg")

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade

    def clean(self):
        if self.produto.tipo =='PR':
            if self.quantidade > self.produto.estoque:
                raise ValidationError(f'Estoque insuficiente para o produto {self.produto.nome}. Estoque disponível: {self.produto.estoque}')
            
    def save(self, *args, **kwargs):
        if not self.pk and self.produto.tipo == 'PR':
            self.produto.estoque -= self.quantidade
            self.produto.save()

        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.quantidade} - {self.produto.nome}"
    
    class Meta:
        verbose_name = "Item da comanda"
        verbose_name_plural = "Itens da comanda"

    


