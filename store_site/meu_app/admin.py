from django.contrib import admin
from .models import Produto, Carrinho, CarrinhoProduto, Comentario

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco')

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)

@admin.register(CarrinhoProduto)
class CarrinhoProdutoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'criado_em')  # Retirei 'avaliacao' temporariamente
    list_filter = ('produto', 'criado_em')  # Ajustado para evitar referência errada
    search_fields = ('usuario__username', 'texto')
