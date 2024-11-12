from .models import Carrinho
from django.db.models import Sum


def carrinho_count(request):
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(usuario=request.user).first()
        if carrinho:
            return {'carrinho_count': carrinho.carrinhoproduto_set.aggregate(total=Sum('quantidade'))['total'] or 0}
    return {'carrinho_count': 0}
