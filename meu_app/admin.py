from django.contrib import admin
from .models import Produto, Carrinho, CarrinhoProduto, Comentario

# Registro do modelo Produto no admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'preco')  # Campos a serem exibidos na lista

# Registro do modelo Carrinho no admin
@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)  # Campos a serem exibidos na lista

# Registro do modelo CarrinhoProduto no admin
@admin.register(CarrinhoProduto)
class CarrinhoProdutoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade')  # Campos a serem exibidos na lista

# Registro do modelo Comentario no admin
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'criado_em')  # Campos a serem exibidos na lista
    list_filter = ('produto', 'criado_em')  # Filtros disponíveis na lista
    search_fields = ('usuario__username', 'texto')  # Campos pesquisáveis
