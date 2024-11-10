# 🧁 **Cupcake App - Gerenciamento de Loja Online**

O **Cupcake App** é uma aplicação Django desenvolvida para gerenciar uma loja online com funcionalidades completas de e-commerce. Este projeto inclui exibição de produtos, carrinho de compras, controle de usuários, avaliações e comentários. Ele foi criado com foco em usabilidade, responsividade e fácil manutenção.

---

## 📋 **Funcionalidades**

- **Catálogo de Produtos**:
  - Exibição detalhada de produtos com imagens, descrição e preço.
  - Avaliações e comentários dos usuários.

- **Carrinho de Compras**:
  - Adicionar, atualizar e remover itens.
  - Cálculo dinâmico de subtotal e total do carrinho.

- **Autenticação de Usuários**:
  - Registro, login e logout de usuários.
  - Gerenciamento de sessão para carrinho personalizado por usuário.

- **Avaliações e Comentários**:
  - Sistema de classificação (1 a 5 estrelas) para produtos.
  - Comentários com data e autor associados.

---

## 🛠️ **Tecnologias Utilizadas**

- **Backend**:
  - [Django](https://www.djangoproject.com/) - Framework web robusto para desenvolvimento rápido.
  - Banco de dados SQLite (substituível por PostgreSQL ou MySQL).
  
- **Frontend**:
  - HTML5, CSS3 e responsividade com Media Queries.
  - Integração com templates Django para renderização dinâmica.

- **Outros**:
  - Sistema de autenticação embutido do Django.
  - Manipulação de arquivos e imagens para produtos.

---

## 🚀 **Como Executar o Projeto**

### Pré-requisitos:
- Python 3.10+ e `pip` instalados.
- Ambiente virtual configurado (opcional, mas recomendado).

### Passo a Passo:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cupcake-app.git
   cd cupcake-app
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
3. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
4. Acesse o app no navegador:
    ```bash
    URL: http://127.0.0.1:8000
