from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('about/', views.about, name='about'),  # Página "Sobre"
    path('carrinho/', views.carrinho, name='carrinho'),  # Página do carrinho
    path('login/', auth_views.LoginView.as_view(template_name='meu_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),  # Página de cadastro
    path('registro/', views.registro, name='registro'),  # Página de registro
    path('produto/<int:produto_id>/', views.produto_detalhes, name='produto_detalhes'),  # Detalhes do produto
    path('adicionar_carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),  # Adicionar ao carrinho
    path('atualizar_quantidade/<int:produto_id>/', views.atualizar_quantidade, name='atualizar_quantidade'),  # Atualizar quantidade
    path('remover_item/<int:produto_id>/', views.remover_item, name='remover_item'),  # Remover item do carrinho
    path('produto/<int:produto_id>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),  # Adicionar comentário
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('processar-pagamento/', views.processar_pagamento, name='processar_pagamento'),
    path('compra-concluida/', views.compra_concluida, name='compra_concluida'),
    path('perfil/', views.perfil, name='perfil'),
]
