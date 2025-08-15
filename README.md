# E-commerce API com Flask

API de e-commerce desenvolvida em **Python** com **Flask**, pronta para testes e uso local.

---

## Tecnologias

- Python 3
- Flask
- Flask SQLAlchemy
- Flask-Login
- Flask-CORS
- SQLite (banco de dados local)
- dotenv (para variáveis de ambiente)
- Swagger (documentação da API)

---

## Pré-requisitos

- Python 3
- Git (opcional, para clonar o repositório)

---

## Instalação

1. **Clonar o repositório**:
```
git clone https://github.com/Ferigoti/flask-ecommerce.git
cd flask-ecommerce
```

2. Criar e ativar o ambiente virtual:
```
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

3. Instalar as dependências:
```
pip install -r requirements.txt
```

4. Copiar o arquivo .env-example como .env e inserir as informações necessárias:
```
cp .env-example .env

```

5. Criar o banco de dados (primeira vez que for rodar):
```
from application import db
db.create_all()
```

Rodando a aplicação
```
python application.py
```

A API estará disponível em:
```
http://127.0.0.1:5000/
```

Endpoints principais

Autenticação

POST /login – Login do usuário

POST /logout – Logout do usuário

Produtos

GET /api/products – Listar produtos

GET /api/products/<id> – Detalhes do produto

POST /api/products/add – Adicionar produto (login required)

PUT /api/products/update/<id> – Atualizar produto (login required)

DELETE /api/products/delete/<id> – Deletar produto (login required)

Carrinho

POST /api/cart/add/<product_id> – Adicionar item ao carrinho (login required)

DELETE /api/cart/remove/<product_id> – Remover item do carrinho (login required)

GET /api/cart – Visualizar carrinho (login required)

POST /api/cart/checkout – Finalizar compra (login required)

Observações

O projeto utiliza SQLite como banco local, não precisa de usuário ou senha.

Para usar outro banco (PostgreSQL, MySQL), altere DATABASE_URL no .env.

As senhas não estão criptografadas — não use em produção.

A documentação da API está em swagger.yaml.
