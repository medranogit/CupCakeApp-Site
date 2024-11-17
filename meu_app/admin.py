from django.contrib import admin
from .models import Produto, Carrinho, CarrinhoProduto, Comentario

# Registro do modelo Produto no admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tamanho', 'preco', 'calorias')
    list_filter = ('tamanho',)
    search_fields = ('titulo', 'descricao', 'ingredientes')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'preco', 'imagem', 'tamanho')
        }),
        ('Ingredientes', {
            'fields': ('ingredientes',),
        }),
        ('Informações Nutricionais', {
            'fields': (
                'calorias',
                'gorduras_totais',
                'gorduras_saturadas',
                'carboidratos',
                'proteinas',
                'fibras',
                'sodio'
            ),
        }),
    )

# Registro do modelo Carrinho no admin
@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    search_fields = ('usuario__username',)

# Registro do modelo CarrinhoProduto no admin
@admin.register(CarrinhoProduto)
class CarrinhoProdutoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade')
    list_filter = ('carrinho__usuario',)
    search_fields = ('produto__titulo',)

# Registro do modelo Comentario no admin
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('produto', 'usuario', 'nota', 'criado_em')
    list_filter = ('produto', 'nota', 'criado_em')
    search_fields = ('usuario__username', 'texto')
    readonly_fields = ('criado_em',)
