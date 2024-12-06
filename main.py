from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()


PRODUTOS = [
    {"id": 1, "nome": "Ração para Cão Adulto", "descricao": "Ração premium para cães adultos", "preco": 129.99, "estoque": 100, "peso_kg": 5, "tipo": "Cão"},
    {"id": 2, "nome": "Ração para Gato Filhote", "descricao": "Ração específica para gatos filhotes", "preco": 79.99, "estoque": 50, "peso_kg": 2, "tipo": "Gato"},
    {"id": 3, "nome": "Ração para Cão Sênior", "descricao": "Ração para cães sêniores com baixo teor de gordura", "preco": 149.99, "estoque": 80, "peso_kg": 7, "tipo": "Cão"}
]

CLIENTES = [
    {"id": 1, "nome": "Pedro Henrique Pereira Facundo", "endereco": "Teofilo Amaro", "telefone": "88999981853"},
    {"id": 2, "nome": "Expedito Farias de Melo", "endereco": "Delfino Alves", "telefone": "88993193034"}
]

PEDIDOS = []

# Modelos
class Produto(BaseModel):
    nome: str
    descricao: Optional[str]
    preco: float
    estoque: int
    peso_kg: float  
    tipo: str 

class Cliente(BaseModel):
    nome: str
    endereco: str
    telefone: str

class ItemPedido(BaseModel):
    produto_id: int
    quantidade: int

class Pedido(BaseModel):
    cliente_id: int
    itens: List[ItemPedido]
    endereco_entrega: str

@app.get("/", tags=["Raiz"])
def raiz():
    return {"message": "Bem-vindo ao sistema de vendas de ração para pets!"}

@app.get("/produtos/{produto_id}", tags=["produtos"])
def obter_produto(produto_id: int):
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.post("/produtos", tags=["produtos"])
def criar_produto(produto: Produto):

    produto_dict = produto.dict()
    produto_dict["id"] = len(PRODUTOS) + 1
    PRODUTOS.append(produto_dict)  
    return produto_dict  


@app.put("/produtos/{produto_id}", tags=["produtos"])
def atualizar_produto(produto_id: int, produto: Produto):
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
        produto["nome"] = produto.dict().get("nome", produto["nome"])
        produto["descricao"] = produto.dict().get("descricao", produto["descricao"])
        produto["preco"] = produto.dict().get("preco", produto["preco"])
        produto["estoque"] = produto.dict().get("estoque", produto["estoque"])
        produto["peso_kg"] = produto.dict().get("peso_kg", produto["peso_kg"])
        produto["tipo"] = produto.dict().get("tipo", produto["tipo"])
    return produto

@app.delete("/produtos/{produto_id}", tags=["produtos"])
def remover_produto(produto_id: int):
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    PRODUTOS.remove(produto)
    return {"message": "Produto removido com sucesso"}


@app.get("/clientes", tags=["clientes"])
def listar_clientes():
    return CLIENTES

@app.get("/clientes/{cliente_id}", tags=["clientes"])
def obter_cliente(cliente_id: int):
    cliente = next((c for c in CLIENTES if c["id"] == cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.post("/clientes", tags=["clientes"])
def criar_cliente(cliente: Cliente):
    cliente_dict = cliente.dict()
    cliente_dict["id"] = len(CLIENTES) + 1
    CLIENTES.append(cliente_dict)
    return cliente_dict

@app.put("/clientes/{cliente_id}", tags=["clientes"])
def atualizar_cliente(cliente_id: int, cliente: Cliente):
    cliente_atualizado = next((c for c in CLIENTES if c["id"] == cliente_id), None)
    if cliente_atualizado is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    

    cliente_atualizado["nome"] = cliente.nome
    cliente_atualizado["endereco"] = cliente.endereco
    cliente_atualizado["telefone"] = cliente.telefone

    return cliente_atualizado


@app.delete("/clientes/{cliente_id}", tags=["clientes"])
def remover_cliente(cliente_id: int):
    cliente = next((c for c in CLIENTES if c["id"] == cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    CLIENTES.remove(cliente)
    return {"message": "Cliente removido com sucesso"}

# Rotas de Pedidos
@app.post("/pedidos", tags=["pedidos"])
def criar_pedido(pedido: Pedido):
    cliente = next((c for c in CLIENTES if c["id"] == pedido.cliente_id), None)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    total = 0
    for item in pedido.itens:
        produto = next((p for p in PRODUTOS if p["id"] == item.produto_id), None)
        if produto is None:
            raise HTTPException(status_code=404, detail=f"Produto com ID {item.produto_id} não encontrado")
        if produto["estoque"] < item.quantidade:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para o produto {produto['nome']}")
        produto["estoque"] -= item.quantidade
        total += produto["preco"] * item.quantidade

    novo_pedido = {
        "id": len(PEDIDOS) + 1,
        "cliente_id": pedido.cliente_id,
        "itens": pedido.itens,
        "endereco_entrega": pedido.endereco_entrega,
        "total": total,
        "status": "Pendente"
    }
    PEDIDOS.append(novo_pedido)
    return novo_pedido

@app.get("/pedidos", tags=["pedidos"])
def listar_pedidos():
    return PEDIDOS
