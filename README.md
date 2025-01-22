# 🧁 **Cupcake App**

Aplicação Django para gerenciamento de uma loja virtual de cupcakes, integrando funcionalidades completas de e-commerce, com foco em experiência do usuário e design responsivo.

---

## 🚀 **Funcionalidades Detalhadas**

### **1. Catálogo de Produtos**
- Apresenta uma lista de cupcakes com:
  - **Imagem**: Exibição visual de cada produto.
  - **Descrição curta**: Texto com informações rápidas.
  - **Preço**: Valor em destaque.
  - **Botões de Ação**:
    - **"Ver Detalhes"**: Redireciona para a página do produto.
    - **"Adicionar ao Carrinho"**: Adiciona o item ao carrinho (com mensagem de feedback).

### **2. Página de Detalhes do Produto**
- Informações completas sobre o cupcake:
  - **Tamanho**: Pequeno, médio ou grande.
  - **Ingredientes**: Lista completa do produto.
  - **Informações Nutricionais**:
    - Calorias, gorduras, carboidratos, proteínas, fibras e sódio.
  - **Seção de Comentários**:
    - Usuários podem avaliar o produto (1 a 5 estrelas) e deixar comentários.

### **3. Carrinho de Compras**
- Recursos do carrinho:
  - **Adicionar Produtos**: Incrementa a quantidade diretamente.
  - **Atualizar Quantidade**: Permite ajustes dinâmicos.
  - **Remover Itens**: Remove produtos do carrinho.
  - **Cálculo de Subtotal e Total Geral**.
  - **Calculadora de Frete**: Simulação do valor com base no CEP.

### **4. Finalização de Compra**
- Página de pagamento:
  - Formulário para entrada de dados de cartão (nome, número, validade e CVV).
  - Opções de parcelamento.
  - Exibição clara do valor total com frete.

### **5. Histórico de Compras**
- Exibido no perfil do usuário:
  - **Protocolo de Pedido**: Número único para referência.
  - **Total Pago**: Valor da compra com frete.
  - **Data e Hora**: Registro do pedido.
  - **Detalhes dos Itens**: Lista completa dos produtos comprados.

### **6. Sistema de Usuários**
- **Autenticação**:
  - Cadastro e login com validações robustas.
  - Redefinição de senha integrada.
- **Gerenciamento de Perfil**:
  - Edição de nome, e-mail, telefone e CEP.
  - Histórico de compras exibido na mesma página.

### **7. Suporte ao Cliente**
- Formulário de contato:
  - Campos para assunto e mensagem.
  - Feedback visual após envio da solicitação.

### **8. Painel Administrativo**
- Funcionalidades para administradores:
  - Gerenciamento de produtos, incluindo upload de imagens e definição de informações nutricionais.
  - Visualização e moderação de comentários.
  - Consulta ao histórico de pedidos.

### **9. Design Responsivo**
- Interface otimizada para desktop e dispositivos móveis.
- Temas claros e escuros ajustáveis pelo usuário.

- 
## ✨ **Instalação**

Siga os passos abaixo para configurar o projeto em sua máquina local:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/medranogit/CupCakeApp-Site.git
   cd CupCakeApp-Site
   ```

2. **Crie um ambiente virtual e ative-o**:
   ```bash
   python -m venv env
   source env/bin/activate  # Para Linux/Mac
   env\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

5. **Acesse a aplicação em seu navegador**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## ⚠️ **ATENÇÃO - No pagamento com cartão coloquem dados não verdadeiros**
