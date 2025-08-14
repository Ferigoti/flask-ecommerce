# API E-commerce com Flask

API simples de e-commerce com Flask, pronta para testes no Postman.

## Rodando o projeto

1. Clone o repositório:
```
git clone https://github.com/Ferigoti/flask-ecommerce.git
cd flask-ecommerce
```
2. Crie e ative o ambiente virtual:

```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Rode a aplicação:

```
python app.py
```

API disponível em: http://127.0.0.1:5000

Testes no Postman
Usuário
Registro: POST /register

Login: POST /login

Logout: POST /logout

Produtos
Adicionar: POST /api/products/add

Atualizar: PUT /api/products/update/<id>

Deletar: DELETE /api/products/delete/<id>

Listar: GET /api/products

Detalhes: GET /api/products/<id>

Carrinho
Adicionar item: POST /api/cart/add/<product_id>

Remover item: DELETE /api/cart/remove/<product_id>

Ver carrinho: GET /api/cart

Checkout: POST /api/cart/checkout

O banco SQLite (ecommerce.db) é criado automaticamente.
