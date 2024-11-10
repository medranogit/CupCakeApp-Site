from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Campo de nota
    criado_em = models.DateTimeField(auto_now_add=True)
    
    
class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='avaliacoes')
    nota = models.PositiveSmallIntegerField()  # Nota de 1 a 5
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario.username} - {self.nota}/5"

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='CarrinhoProduto')

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class CarrinhoProduto(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return f"{self.produto.titulo} ({self.quantidade})"

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="compras")
    protocolo = models.CharField(max_length=20, unique=True)
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    detalhes = models.TextField(blank=True, null=True)  # Informações adicionais

    def __str__(self):
        return f"{self.protocolo} - {self.usuario.username}"
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"