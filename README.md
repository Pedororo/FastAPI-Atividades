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
   [git clone https://github.com/seu-usuario/sistema-racao-pets.git](https://github.com/Pedororo/FastAPI-Atividades)

   ## Testando a API com Postman

Para facilitar o teste da API, você pode usar o **Postman**. Para isso, basta importar a coleção de requisições.

1. **Baixe o arquivo de coleção do Postman** [aqui](<[COLECAO_DO_POSTMAN_URL](https://web.postman.co/workspace/409f7473-f1fb-4527-877f-988c4ecc66bd/collection/40242821-0dd90384-710d-4683-8034-dd0f233c0025)>).
   
2. **Importe a coleção**:
   - Abra o Postman.
   - Clique em "Import" no canto superior esquerdo.
   - Selecione o arquivo de coleção baixado.
   
3. **Use as rotas da API**:
   Após importar a coleção, você terá acesso a todas as rotas descritas anteriormente, como produtos, clientes e pedidos, com exemplos de requisições e respostas.

Com o Postman, você poderá testar a criação, leitura, atualização e exclusão de produtos, clientes e pedidos diretamente de uma interface amigável.

> Lembre-se de que o servidor deve estar rodando localmente (`http://127.0.0.1:8000`) para que as requisições funcionem corretamente.

