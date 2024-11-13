from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

# Nomes das URLs
INDEX = 'index'
ABOUT = 'about'
CARRINHO = 'carrinho'
LOGIN = 'login'
LOGOUT = 'logout'
SIGNUP = 'signup'
REGISTRO = 'registro'
PRODUTO_DETALHES = 'produto_detalhes'
ADICIONAR_CARRINHO = 'adicionar_carrinho'
ATUALIZAR_QUANTIDADE = 'atualizar_quantidade'
REMOVER_ITEM = 'remover_item'
ADICIONAR_COMENTARIO = 'adicionar_comentario'
FINALIZAR_COMPRA = 'finalizar_compra'
PROCESSAR_PAGAMENTO = 'processar_pagamento'
COMPRA_CONCLUIDA = 'compra_concluida'
PERFIL = 'perfil'
SUPORTE = 'suporte'

urlpatterns = [
    # Páginas principais
    path('', views.home, name=INDEX),  # Página inicial
    path('about/', views.about, name=ABOUT),  # Página "Sobre"
    
    # Carrinho
    path('carrinho/', views.carrinho, name=CARRINHO),  # Página do carrinho
    path('adicionar_carrinho/<int:produto_id>/', views.adicionar_carrinho, name=ADICIONAR_CARRINHO),  # Adicionar ao carrinho
    path('atualizar_quantidade/<int:produto_id>/', views.atualizar_quantidade, name=ATUALIZAR_QUANTIDADE),  # Atualizar quantidade
    path('remover_item/<int:produto_id>/', views.remover_item, name=REMOVER_ITEM),  # Remover item do carrinho
    
    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='meu_app/login.html'), name=LOGIN),  # Página de login
    path('logout/', LogoutView.as_view(next_page=INDEX), name=LOGOUT),  # Logout e redirecionamento
    path('signup/', views.signup, name=SIGNUP),  # Página de cadastro
    path('registro/', views.registro, name=REGISTRO),  # Página de registro
    
    # Produtos
    path('produto/<int:produto_id>/', views.produto_detalhes, name=PRODUTO_DETALHES),  # Detalhes do produto
    path('produto/<int:produto_id>/comentar/', views.adicionar_comentario, name=ADICIONAR_COMENTARIO),  # Adicionar comentário
    
    # Finalização de compra
    path('finalizar-compra/', views.finalizar_compra, name=FINALIZAR_COMPRA),  # Finalizar compra
    path('processar-pagamento/', views.processar_pagamento, name=PROCESSAR_PAGAMENTO),  # Processar pagamento
    path('compra-concluida/', views.compra_concluida, name=COMPRA_CONCLUIDA),  # Compra concluída
    
    # Perfil e suporte
    path('perfil/', views.perfil, name=PERFIL),  # Página de perfil
    path('suporte/', views.suporte, name=SUPORTE),  # Página de suporte
]
