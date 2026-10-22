from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="API de Produtos - SENAI",
    description="API didática para operações CRUD de produtos.",
    version="1.0.0",
)


class ProdutoEntrada(BaseModel):
    nome: str = Field(min_length=1, max_length=100, description="Nome do produto")


class Produto(ProdutoEntrada):
    id: int


produtos: dict[int, Produto] = {
    1: Produto(id=1, nome="Maçã"),
    2: Produto(id=2, nome="Goiaba"),
    3: Produto(id=3, nome="Melancia"),
    4: Produto(id=4, nome="Banana"),
    5: Produto(id=5, nome="Melão"),
}


@app.get("/", tags=["Geral"], summary="Mensagem de boas-vindas")
def inicio():
    return {"mensagem": "Bem-vindo à API de produtos do SENAI"}


@app.get(
    "/produtos",
    response_model=list[Produto],
    tags=["Produtos"],
    summary="Listar produtos",
)
def listar_produtos():
    return list(produtos.values())


@app.get(
    "/produtos/{produto_id}",
    response_model=Produto,
    tags=["Produtos"],
    summary="Consultar um produto",
)
def buscar_produto(produto_id: int):
    produto = produtos.get(produto_id)
    if produto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )
    return produto


@app.post(
    "/produtos",
    response_model=Produto,
    status_code=status.HTTP_201_CREATED,
    tags=["Produtos"],
    summary="Cadastrar um produto",
)
def criar_produto(dados: ProdutoEntrada):
    produto_id = max(produtos, default=0) + 1
    produto = Produto(id=produto_id, nome=dados.nome)
    produtos[produto_id] = produto
    return produto


@app.put(
    "/produtos/{produto_id}",
    response_model=Produto,
    tags=["Produtos"],
    summary="Atualizar um produto",
)
def atualizar_produto(produto_id: int, dados: ProdutoEntrada):
    if produto_id not in produtos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )

    produto = Produto(id=produto_id, nome=dados.nome)
    produtos[produto_id] = produto
    return produto


@app.delete(
    "/produtos/{produto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    tags=["Produtos"],
    summary="Remover um produto",
)
def excluir_produto(produto_id: int):
    if produto_id not in produtos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )

    del produtos[produto_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)