from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()


products = []

@app.get("/products")
async def list_products():
    """
    Recuperar a lista de produtos.
    """
    return {
        "status": "sucesso",
        "message": "Produtos recuperados com sucesso.",
        "data": products
    }

@app.get("/products/{product_id}")
async def get_product_by_id(product_id: int):
    """
    Recuperar um produto pelo seu ID.
    """
    for product in products:
        if product["id"] == product_id:
            return {
                "status": "sucesso",
                "message": "Produto recuperado com sucesso.",
                "data": product
            }
    raise HTTPException(status_code=404, detail="Produto não encontrado.")

@app.get("/products_search")
async def search_products_by_name(name: str = Query(...)):
    """
    Pesquisar produtos pelo nome.
    """
    matching_products = [product for product in products if name.lower() in product["name"].lower()]
    if matching_products:
        return {
            "status": "sucesso",
            "message": "Produtos recuperados com sucesso.",
            "data": matching_products
        }
    raise HTTPException(status_code=404, detail="Nenhum produto encontrado com o nome fornecido.")

@app.post("/products")
async def create_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...)
):
    """
    Adicionar um novo produto à lista.
    """
    product = {
        "id": len(products) + 1,  
        "name": name,
        "description": description,
        "price": price,
        "stock": stock
    }
    products.append(product)
    return {
        "status": "sucesso",
        "message": "Produto adicionado com sucesso.",
        "data": product
    }

@app.put("/products/{product_id}")
async def update_product(
    product_id: int,
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...)
):
    """
    Atualizar os detalhes de um produto pelo ID.
    """
    for product in products:
        if product["id"] == product_id:
            product.update({"name": name, "description": description, "price": price, "stock": stock})
            return {
                "status": "sucesso",
                "message": "Produto atualizado com sucesso.",
                "data": product
            }
    raise HTTPException(status_code=404, detail="Produto não encontrado.")

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    """
    Excluir um produto pelo seu ID.
    """
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            return {
                "status": "sucesso",
                "message": "Produto excluído com sucesso.",
                "data": deleted_product
            }
    raise HTTPException(status_code=404, detail="Produto não encontrado.")
