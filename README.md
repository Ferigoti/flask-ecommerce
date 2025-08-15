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

## Estrutura do projeto

E-COMMERCE-PROJECT/
│
├─ instance/
│ └─ ecommerce.db # Banco de dados SQLite
│
├─ .env-example # Modelo do arquivo .env
├─ application.py # Aplicação principal
├─ requirements.txt # Dependências do projeto
├─ swagger.yaml # Documentação da API
└─ .gitignore

---

## Pré-requisitos

- Python 3
- Git (opcional, para clonar o repositório)

---

## Instalação

1. **Clonar o repositório**:
```
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
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

4. Criar o arquivo .env com base no .env-example:
```
SECRET_KEY=minha_chave_123
DATABASE_URL=sqlite:///instance/ecommerce.db
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
