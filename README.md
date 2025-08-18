# API de E-commerce em Flask

![Linguagem](https://img.shields.io/badge/Python-3.11-blue.svg)
![Framework](https://img.shields.io/badge/Flask-3.0-lightgrey.svg)
![Licença](https://img.shields.io/badge/license-MIT-green)

## 📖 Sobre o Projeto

Esta é uma API RESTful para um sistema de e-commerce desenvolvida em Python com o framework Flask. O projeto serve como um backend robusto para gerenciar usuários, produtos e carrinhos de compras, seguindo as melhores práticas de desenvolvimento, como a estrutura de *Application Factory* e *Blueprints* para organização do código.

Este projeto foi criado para demonstrar habilidades em desenvolvimento de APIs, modelagem de dados e autenticação de usuários.

---

## ✨ Funcionalidades

- **Autenticação de Usuários**: Sistema de login e logout baseado em sessão. Rotas protegidas que exigem autenticação.
- **Gerenciamento de Produtos (CRUD)**:
  - Adicionar novos produtos.
  - Visualizar todos os produtos ou um produto específico.
  - Atualizar informações de um produto.
  - Remover produtos.
- **Gerenciamento de Carrinho de Compras**:
  - Adicionar itens ao carrinho de um usuário autenticado.
  - Visualizar o conteúdo do carrinho.
  - Remover itens do carrinho.
  - Realizar um "checkout" (limpando o carrinho).

---

## 🛠️ Tecnologias Utilizadas

- **Backend**:
  - **Python 3**
  - **Flask**: Micro-framework para a construção da API.
  - **Flask-SQLAlchemy**: ORM para interação com o banco de dados.
  - **Flask-Login**: Gerenciamento de sessão e autenticação de usuários.
  - **Flask-CORS**: Para permitir requisições de diferentes origens (front-end).
  - **python-dotenv**: Para gerenciamento de variáveis de ambiente.
- **Banco de Dados**:
  - **SQLite**: Banco de dados padrão para desenvolvimento.
- **Ferramentas**:
  - **Postman**: Utilizado para testar e interagir com os endpoints da API.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

### Pré-requisitos

- **Python 3.9+**
- **pip** (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**


```Bash
git clone https://github.com/Ferigoti/flask-ecommerce.git
cd flask-ecommerce
Crie e ative um ambiente virtual:
```

2. Crie e ative um ambiente virtual:
```Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```Bash

pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie uma cópia do arquivo .env-example e renomeie para .env. Os valores padrão são suficientes para rodar localmente.

```Bash

# Windows
copy .env-example .env

# macOS / Linux
cp .env-example .env
```

5. Execute a aplicação:
```Bash
python run.py
```

- Na primeira vez que a aplicação for executada, o banco de dados `ecommerce.db` será criado automaticamente na raiz do projeto.
- Além disso, um **usuário administrador padrão** é inserido no banco para facilitar os testes:
  - **Usuário**: `admin`
  - **Senha**: `123`
- A API estará rodando em `http://127.0.0.1:5000`.

## ⚡ Usando a API com Postman

A melhor forma de testar a API é através do Postman.

**Dica Importante:** O Postman gerencia cookies de sessão automaticamente. Após fazer uma requisição de `POST /login` com sucesso, ele salvará o cookie de autenticação e o enviará nas requisições seguintes, permitindo o acesso às rotas protegidas.

### Endpoints da API

#### Autenticação

- `POST /login`
  - **Descrição**: Autentica um usuário e inicia uma sessão.
  - **Usuário Administrador Padrão (criado na primeira execução)**:
    - **username**: `admin`
    - **password**: `123`
  - **Body (JSON)**:
    ```json
    {
      "username": "admin",
      "password": "123"
    }
    ```
- `POST /logout`
  - **Descrição**: Encerra a sessão do usuário. Requer autenticação.

#### Produtos (requer autenticação para `POST`, `PUT`, `DELETE`)

- `GET /api/products`
  - **Descrição**: Retorna uma lista de todos os produtos.
- `GET /api/products/<int:product_id>`
  - **Descrição**: Retorna os detalhes de um produto específico.
- `POST /api/products/add`
  - **Descrição**: Adiciona um novo produto.
  - **Body (JSON)**:
    ```json
    {
      "name": "Notebook Gamer",
      "price": 5999.90,
      "description": "Notebook com placa de vídeo dedicada."
    }
    ```
- `PUT /api/products/update/<int:product_id>`
  - **Descrição**: Atualiza um produto existente.
- `DELETE /api/products/delete/<int:product_id>`
  - **Descrição**: Deleta um produto.

#### Carrinho (requer autenticação)

- `GET /api/cart`
  - **Descrição**: Exibe todos os itens no carrinho do usuário logado.
- `POST /api/cart/add/<int:product_id>`
  - **Descrição**: Adiciona um produto ao carrinho.
- `DELETE /api/cart/remove/<int:product_id>`
  - **Descrição**: Remove um item do carrinho.
- `POST /api/cart/checkout`
  - **Descrição**: Finaliza a compra e limpa o carrinho.

---

## ✒️ Autor

Feito com ❤️ por **João Ferigoti**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joao-ferigoti/)

---

## 📄 Licença

Este projeto está sob a licença MIT.