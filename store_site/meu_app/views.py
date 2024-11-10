from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .models import Produto, Comentario, Avaliacao, Carrinho, CarrinhoProduto
from .forms import RegistroForm, ComentarioForm, AvaliacaoForm
from django.db.models import Sum  # Import para somar as quantidades no carrinho
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import random
import re
from django.contrib import messages
from random import randint, uniform
from decimal import Decimal


def home(request):
    """Exibe a página inicial com a lista de produtos."""
    produtos = Produto.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'meu_app/home.html', {'produtos': produtos})


def produto_detalhes(request, produto_id):
    """Exibe os detalhes de um produto específico."""
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'meu_app/produto_detalhes.html', {'produto': produto})


@login_required
@require_POST
def adicionar_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    carrinho_produto, created = CarrinhoProduto.objects.get_or_create(carrinho=carrinho, produto=produto)

    if not created:
        carrinho_produto.quantidade += 1
    carrinho_produto.save()

    total_itens = carrinho.carrinhoproduto_set.aggregate(total=Sum('quantidade'))['total'] or 0

    return JsonResponse({"message": "Produto adicionado com sucesso!", "total_itens": total_itens})


def about(request):
    """Exibe a página 'Sobre'."""
    return render(request, 'meu_app/about.html')

@login_required
def carrinho(request):
    """Exibe a página do carrinho com os itens do usuário e calcula o frete."""
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    itens = []
    total_geral = Decimal(0.0)
    frete = None
    erro_cep = None
    total_com_frete = None

    if carrinho:
        itens = carrinho.carrinhoproduto_set.all()
        total_geral = sum(item.subtotal for item in itens)

    if request.method == 'POST' and 'calcular_frete' in request.POST:
        cep = request.POST.get('cep', '').strip()
        if len(cep) == 9:  # Validação básica para "XXXXX-XXX"
            frete = Decimal(f"{uniform(10, 15):.2f}")  # Valor gerado como Decimal
            total_com_frete = total_geral + frete  # Soma o frete ao total
        else:
            erro_cep = "CEP inválido. Por favor, insira um CEP no formato XXXXX-XXX."

    return render(request, 'meu_app/carrinho.html', {
        'carrinho': carrinho,
        'itens': itens,
        'total_geral': total_geral,
        'frete': frete,
        'total_com_frete': total_com_frete,  # Inclui total com frete
        'erro_cep': erro_cep
    })

@login_required
def atualizar_quantidade(request, produto_id):
    """Atualiza a quantidade de um item no carrinho."""
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    if carrinho:
        carrinho_produto = CarrinhoProduto.objects.filter(carrinho=carrinho, produto=produto).first()
        if carrinho_produto:
            quantidade = int(request.POST.get('quantidade', 1))
            if quantidade > 0:
                carrinho_produto.quantidade = quantidade
                carrinho_produto.save()
            else:
                carrinho_produto.delete()  # Remove o item se a quantidade for zero
    return redirect('carrinho')


@login_required
def remover_item(request, produto_id):
    """Remove um item do carrinho."""
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    if carrinho:
        CarrinhoProduto.objects.filter(carrinho=carrinho, produto=produto).delete()
    return redirect('carrinho')


def carrinho_count(request):
    """Adiciona a contagem de produtos no carrinho ao contexto global."""
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
        if carrinho:
            total_produtos = carrinho.carrinhoproduto_set.aggregate(total_produtos=Sum('quantidade'))['total_produtos'] or 0
            return {'carrinho_count': total_produtos}
    return {'carrinho_count': 0}

def signup(request):
    """Exibe a página de cadastro."""
    return render(request, 'meu_app/signup.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'meu_app/registro.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'meu_app/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'meu_app/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def produto_detalhes(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    comentarios = produto.comentarios.all()
    avaliacoes = produto.avaliacoes.all()
    media_avaliacoes = avaliacoes.aggregate(media=Avg('nota'))['media'] or 0

    if request.method == 'POST':
        if 'comentario_submit' in request.POST:
            comentario_form = ComentarioForm(request.POST)
            if comentario_form.is_valid():
                comentario = comentario_form.save(commit=False)
                comentario.usuario = request.user
                comentario.produto = produto
                comentario.save()
                return redirect('produto_detalhes', produto_id=produto.id)
        elif 'avaliacao_submit' in request.POST:
            avaliacao_form = AvaliacaoForm(request.POST)
            if avaliacao_form.is_valid():
                avaliacao = avaliacao_form.save(commit=False)
                avaliacao.usuario = request.user
                avaliacao.produto = produto
                avaliacao.save()
                return redirect('produto_detalhes', produto_id=produto.id)
    else:
        comentario_form = ComentarioForm()
        avaliacao_form = AvaliacaoForm()

    context = {
        'produto': produto,
        'comentarios': comentarios,
        'media_avaliacoes': media_avaliacoes,
        'comentario_form': comentario_form,
        'avaliacao_form': avaliacao_form,
    }
    return render(request, 'meu_app/produto_detalhes.html', context)

@login_required
def adicionar_comentario(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        nota = request.POST.get('nota')  # Certifique-se de que o formulário está enviando este campo
        Comentario.objects.create(
            produto=produto,
            usuario=request.user,
            texto=texto,
            nota=int(nota) if nota else None,  # Converte para inteiro, se fornecido
        )
    return redirect('produto_detalhes', produto_id=produto.id)

@login_required
def finalizar_compra(request):
    """Exibe uma página fake de pagamento."""
    carrinho = Carrinho.objects.filter(usuario=request.user).first()
    total_geral = 0

    if carrinho:
        itens = carrinho.carrinhoproduto_set.all()
        total_geral = sum(item.subtotal for item in itens)

    return render(request, 'meu_app/pagamento.html', {'total_geral': total_geral})

@login_required
def processar_pagamento(request):
    if request.method == 'POST':
        nome_cartao = request.POST.get('nome_cartao')
        numero_cartao = request.POST.get('numero_cartao')
        validade = request.POST.get('validade')
        cvv = request.POST.get('cvv')
        parcelas = request.POST.get('parcelas')

        # Recuperar o carrinho do usuário
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
        if carrinho:
            itens = carrinho.carrinhoproduto_set.all()
            total_geral = sum(item.subtotal for item in itens)  # Soma os subtotais
            frete = Decimal(uniform(10, 15))  # Converte para Decimal
            total_com_frete = total_geral + frete  # Soma o frete ao total

            # Simulação de processamento do pagamento
            if nome_cartao and numero_cartao and validade and cvv:
                # Esvaziar o carrinho
                carrinho.carrinhoproduto_set.all().delete()

                # Converte total para float antes de salvar na sessão
                request.session['total_com_frete'] = float(total_com_frete)

                return redirect('compra_concluida')
            else:
                messages.error(request, 'Erro ao processar pagamento. Verifique os dados e tente novamente.')
                return redirect('finalizar_compra')
    return redirect('finalizar_compra')

@login_required
def compra_concluida(request):
    """Exibe uma página de confirmação de compra com número de protocolo e total."""
    protocolo = f"PROTO-{randint(100000, 999999)}"  # Gera um número aleatório
    total_com_frete = request.session.get('total_com_frete', 0)  # Recupera o total da sessão
    return render(request, 'meu_app/compra_concluida.html', {
        'protocolo': protocolo,
        'total_com_frete': total_com_frete
    })
