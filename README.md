# Sistema de Vendas de Ração para Pets

Este projeto é um sistema simples de vendas de ração para pets utilizando o **FastAPI**. Ele simula a gestão de produtos (ração), clientes e pedidos, permitindo criar, atualizar, listar e remover produtos, clientes e pedidos. A seguir, estão descritas as principais funcionalidades da API.

## Endpoints Disponíveis

### 1. Produtos
- **GET /produtos/{produto_id}**
  - Retorna as informações de um produto específico pelo seu `produto_id`.
- **POST /produtos**
  - Cria um novo produto.
  - **Body** (JSON):
    ```json
    {
      "nome": "Ração para Cão Adulto",
      "descricao": "Ração premium para cães adultos",
      "preco": 129.99,
      "estoque": 100,
      "peso_kg": 5,
      "tipo": "Cão"
    }
    ```
- **PUT /produtos/{produto_id}**
  - Atualiza as informações de um produto específico pelo seu `produto_id`.
  - **Body** (JSON):
    ```json
    {
      "nome": "Ração para Cão Adulto",
      "descricao": "Nova descrição",
      "preco": 139.99,
      "estoque": 120,
      "peso_kg": 5,
      "tipo": "Cão"
    }
    ```
- **DELETE /produtos/{produto_id}**
  - Remove um produto específico pelo seu `produto_id`.

### 2. Clientes
- **GET /clientes**
  - Retorna a lista de todos os clientes.
- **GET /clientes/{cliente_id}**
  - Retorna as informações de um cliente específico pelo seu `cliente_id`.
- **POST /clientes**
  - Cria um novo cliente.
  - **Body** (JSON):
    ```json
    {
      "nome": "Pedro Henrique",
      "endereco": "Rua Exemplo, 123",
      "telefone": "88999981853"
    }
    ```
- **PUT /clientes/{cliente_id}**
  - Atualiza as informações de um cliente específico pelo seu `cliente_id`.
  - **Body** (JSON):
    ```json
    {
      "nome": "Pedro Henrique Pereira Facundo",
      "endereco": "Rua Alterada, 456",
      "telefone": "88999981853"
    }
    ```
- **DELETE /clientes/{cliente_id}**
  - Remove um cliente específico pelo seu `cliente_id`.

### 3. Pedidos
- **POST /pedidos**
  - Cria um novo pedido.
  - **Body** (JSON):
    ```json
    {
      "cliente_id": 1,
      "itens": [
        {"produto_id": 1, "quantidade": 2},
        {"produto_id": 2, "quantidade": 1}
      ],
      "endereco_entrega": "Rua de Entrega, 789"
    }
    ```
- **GET /pedidos**
  - Retorna a lista de todos os pedidos.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sistema-racao-pets.git
